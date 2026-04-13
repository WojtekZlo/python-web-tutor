from datetime import timedelta
import ast
import json
import math
import os
import random
import shlex
import subprocess
import sys
import tempfile
import threading

from flask import Flask, jsonify, render_template, request, session

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from lessons import LESSONS as RAW_LESSONS

MAX_LESSON_ID = int(os.getenv("MAX_LESSON_ID", "100"))
LESSONS = [lesson for lesson in RAW_LESSONS if int(lesson.get("id", 0)) <= MAX_LESSON_ID]

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY", "super-secret-bioinfo-key")
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    PERMANENT_SESSION_LIFETIME=timedelta(days=30),
)

TEST_SIZE = 30

LANGUAGE_FIXES = {
    "Guanjn": "Guaniny",
    "nukelotyd": "nukleotyd",
    "uzyciem": "użyciem",
    "sukce": "sukces",
    "Sprobuj": "Spróbuj",
    "sprobuj": "spróbuj",
}

STATIC_USERS = {f"user{i}": "123" for i in range(1, 11)}
PROGRESS_FILE_PATH = os.path.join(BASE_DIR, "user_progress.json")
PROGRESS_LOCK = threading.Lock()


def _default_user_state():
    return {
        "current_lesson_index": 0,
        "test_mode": False,
        "test_question_indices": [],
        "test_position": 0,
        "test_results": [],
        "test_section_stats": {},
    }


def _merge_state_with_defaults(state):
    defaults = _default_user_state()
    if not isinstance(state, dict):
        return defaults

    merged = dict(defaults)
    for key in defaults:
        if key in state:
            merged[key] = state[key]

    if not isinstance(merged["current_lesson_index"], int):
        merged["current_lesson_index"] = 0
    if not isinstance(merged["test_mode"], bool):
        merged["test_mode"] = False
    if not isinstance(merged["test_question_indices"], list):
        merged["test_question_indices"] = []
    if not isinstance(merged["test_position"], int):
        merged["test_position"] = 0
    if not isinstance(merged["test_results"], list):
        merged["test_results"] = []
    if not isinstance(merged["test_section_stats"], dict):
        merged["test_section_stats"] = {}

    return merged


def _load_progress_store():
    if not os.path.exists(PROGRESS_FILE_PATH):
        return {}

    try:
        with open(PROGRESS_FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return data
    except (OSError, json.JSONDecodeError):
        pass

    return {}


def _save_progress_store(store):
    tmp_path = f"{PROGRESS_FILE_PATH}.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(store, f, ensure_ascii=False, indent=2)
    os.replace(tmp_path, PROGRESS_FILE_PATH)


def _load_state_for_user(username):
    with PROGRESS_LOCK:
        store = _load_progress_store()
        return _merge_state_with_defaults(store.get(username))


def _persist_state_for_user(username, state):
    with PROGRESS_LOCK:
        store = _load_progress_store()
        store[username] = _merge_state_with_defaults(state)
        _save_progress_store(store)


def _current_user():
    return session.get("username")


def _is_logged_in():
    username = _current_user()
    return bool(username and username in STATIC_USERS)


def _get_state():
    if not _is_logged_in():
        return None

    state = session.get("state")
    if not isinstance(state, dict):
        state = _load_state_for_user(_current_user())

    state = _merge_state_with_defaults(state)
    session["state"] = state
    session.modified = True
    return state


def _save_state(state):
    if not _is_logged_in():
        return

    normalized = _merge_state_with_defaults(state)
    session["state"] = normalized
    session.modified = True
    _persist_state_for_user(_current_user(), normalized)


def _reset_test_state(state):
    state["test_mode"] = False
    state["test_question_indices"] = []
    state["test_position"] = 0
    state["test_results"] = []
    state["test_section_stats"] = {}


def _clean_language(text):
    if not text:
        return text

    fixed = text
    for old, new in LANGUAGE_FIXES.items():
        fixed = fixed.replace(old, new)
    return fixed


def _normalize_lesson_text(value):
    if isinstance(value, str):
        return value
    if isinstance(value, (list, tuple)):
        return "".join(_normalize_lesson_text(item) for item in value)
    if value is None:
        return ""
    return str(value)


def _lesson_for_view(lesson):
    return {
        **lesson,
        "title": _clean_language(_normalize_lesson_text(lesson.get("title", ""))),
        "description": _clean_language(_normalize_lesson_text(lesson.get("description", ""))),
        "initial_code": _clean_language(_normalize_lesson_text(lesson.get("initial_code", ""))),
    }


def _lesson_section(lesson):
    title = lesson.get("title", "").lower()
    lesson_id = lesson.get("id", 0)

    if "lekcja teoretyczna" in title:
        return "Teoria"
    if "sprawdzian" in title:
        return "Sprawdziany przekrojowe"
    if title.startswith("wiz"):
        return "Wizualizacja"
    if title.startswith("ml"):
        return "Machine Learning"
    if "instalacje" in title or "setup" in title:
        return "Instalacja i środowisko"
    if "workflow" in title or "integracja" in title or "pipeline" in title or "subprocess" in title:
        return "Integracja narzędzi i pipeline"
    if "fasta" in title or "vcf" in title or "tsv" in title or "csv" in title or "plik" in title:
        return "Pliki i formaty danych"
    if "feature" in title or "cech" in title:
        return "Feature Engineering"

    if lesson_id <= 20:
        return "Podstawy Pythona i DNA"
    if lesson_id <= 40:
        return "Pętle, funkcje i struktury"
    if lesson_id <= 70:
        return "Analiza danych i raportowanie"
    if lesson_id <= 100:
        return "Integracja i mini pipeline"
    return "Zaawansowane zadania"


def _build_test_report(state):
    asked = len(state["test_results"])
    correct = sum(1 for item in state["test_results"] if item["correct"])
    percent = (100.0 * correct / asked) if asked else 0.0

    lines = [
        "Losowy test 30 pytań - raport",
        f"Wynik: {correct}/{asked} ({percent:.1f}%)",
        "",
        "Działy wymagające powtórki:",
    ]

    weak = []
    for section, stats in state["test_section_stats"].items():
        total = stats["total"]
        wrong = stats["wrong"]
        if wrong > 0 and total > 0:
            weak.append((wrong / total, wrong, total, section))

    weak.sort(reverse=True)

    if not weak:
        lines.append("- Brak słabych działów. Świetny wynik.")
    else:
        for _, wrong, total, section in weak:
            lines.append(f"- {section}: {wrong}/{total} błędów")

    return "\n".join(lines)


def _normalize_lines(text):
    return [line.strip() for line in text.splitlines() if line.strip()]


def _parse_number(value):
    try:
        return float(value)
    except ValueError:
        return None


def _numbers_close(a, b):
    return math.isclose(float(a), float(b), rel_tol=1e-6, abs_tol=1e-2)


def _compare_values(expected_value, actual_value):
    if isinstance(expected_value, (int, float)) and isinstance(actual_value, (int, float)):
        return _numbers_close(expected_value, actual_value)

    if isinstance(expected_value, set) and isinstance(actual_value, set):
        return expected_value == actual_value

    if isinstance(expected_value, (list, tuple)) and isinstance(actual_value, (list, tuple)):
        if len(expected_value) != len(actual_value):
            return False
        return all(_compare_values(e, a) for e, a in zip(expected_value, actual_value))

    if isinstance(expected_value, dict) and isinstance(actual_value, dict):
        if set(expected_value.keys()) != set(actual_value.keys()):
            return False
        return all(_compare_values(expected_value[k], actual_value[k]) for k in expected_value)

    return str(expected_value).strip() == str(actual_value).strip()


def _compare_line(expected_line, actual_line):
    expected_num = _parse_number(expected_line)
    actual_num = _parse_number(actual_line)
    if expected_num is not None and actual_num is not None:
        return _numbers_close(expected_num, actual_num)

    try:
        expected_literal = ast.literal_eval(expected_line)
        actual_literal = ast.literal_eval(actual_line)
        return _compare_values(expected_literal, actual_literal)
    except (ValueError, SyntaxError):
        pass

    try:
        expected_cmd = shlex.split(expected_line)
        actual_cmd = shlex.split(actual_line)
        if expected_cmd == actual_cmd:
            return True
    except ValueError:
        pass

    expected_tokens = expected_line.split()
    actual_tokens = actual_line.split()
    if len(expected_tokens) == len(actual_tokens):
        token_match = True
        for expected_token, actual_token in zip(expected_tokens, actual_tokens):
            exp_num = _parse_number(expected_token)
            act_num = _parse_number(actual_token)
            if exp_num is not None and act_num is not None:
                if not _numbers_close(exp_num, act_num):
                    token_match = False
                    break
            elif expected_token != actual_token and expected_token.lower() != actual_token.lower():
                token_match = False
                break
        if token_match:
            return True

    if "," in expected_line and "," in actual_line and "[" not in expected_line and "[" not in actual_line:
        expected_items = sorted(item.strip().lower() for item in expected_line.split(",") if item.strip())
        actual_items = sorted(item.strip().lower() for item in actual_line.split(",") if item.strip())
        if expected_items == actual_items:
            return True

    return expected_line.strip() == actual_line.strip()


def is_acceptable_output(expected_output, actual_output):
    expected_lines = _normalize_lines(expected_output)
    actual_lines = _normalize_lines(actual_output)

    if len(expected_lines) != len(actual_lines):
        return False

    for expected_line, actual_line in zip(expected_lines, actual_lines):
        if not _compare_line(expected_line, actual_line):
            return False

    return True


def _active_lesson_and_number(state):
    if state["test_mode"]:
        if not state["test_question_indices"] or state["test_position"] >= len(state["test_question_indices"]):
            return None, 0, len(state["test_question_indices"])
        idx = state["test_question_indices"][state["test_position"]]
        return LESSONS[idx], state["test_position"] + 1, len(state["test_question_indices"])

    if state["current_lesson_index"] >= len(LESSONS):
        return None, len(LESSONS), len(LESSONS)
    return LESSONS[state["current_lesson_index"]], state["current_lesson_index"] + 1, len(LESSONS)


def _unauthorized_json():
    return jsonify({"success": False, "message": "Najpierw zaloguj się.", "reload": True}), 401


@app.route('/health')
def health():
    return jsonify({"status": "ok", "lessons": len(LESSONS), "max_lesson_id": MAX_LESSON_ID})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or {}
    username = str(data.get("username", "")).strip().lower()
    password = str(data.get("password", ""))

    if username not in STATIC_USERS or STATIC_USERS[username] != password:
        return jsonify({"success": False, "message": "Niepoprawny login lub hasło."}), 401

    session.clear()
    session.permanent = True
    session["username"] = username
    session["state"] = _load_state_for_user(username)
    session.modified = True

    return jsonify({"success": True, "username": username})


@app.route('/logout', methods=['POST'])
def logout():
    if _is_logged_in() and isinstance(session.get("state"), dict):
        _persist_state_for_user(_current_user(), session.get("state"))

    session.clear()
    return jsonify({"success": True})


@app.route('/')
def index():
    if not _is_logged_in():
        return render_template(
            'index.html',
            login_required=True,
            demo_users=sorted(STATIC_USERS.keys()),
            demo_password='123',
        )

    state = _get_state()

    if state["test_mode"] and state["test_position"] >= len(state["test_question_indices"]):
        report_lesson = {
            "title": "Raport losowego testu 30 pytań",
            "description": _build_test_report(state),
            "initial_code": "# Kliknij 'Zakończ test', aby wrócić do kursu",
        }
        return render_template(
            'index.html',
            login_required=False,
            username=_current_user(),
            lesson=_lesson_for_view(report_lesson),
            lesson_num=len(state["test_question_indices"]),
            total=len(state["test_question_indices"]),
            in_test_mode=True,
            test_finished=True,
        )

    lesson, lesson_num, total = _active_lesson_and_number(state)

    if lesson is None:
        lesson = {
            "title": "Koniec kursu!",
            "description": "Gratulacje bioinformatyku! Przeszedłeś wszystkie dostępne lekcje.",
            "initial_code": "print('Kurs ukończony pomyślnie!')",
        }
        return render_template(
            'index.html',
            login_required=False,
            username=_current_user(),
            lesson=_lesson_for_view(lesson),
            lesson_num=len(LESSONS),
            total=len(LESSONS),
            in_test_mode=False,
            test_finished=False,
        )

    return render_template(
        'index.html',
        login_required=False,
        username=_current_user(),
        lesson=_lesson_for_view(lesson),
        lesson_num=lesson_num,
        total=total,
        in_test_mode=state["test_mode"],
        test_finished=False,
    )


@app.route('/run', methods=['POST'])
def run_code():
    state = _get_state()
    if state is None:
        return _unauthorized_json()

    lesson, _, _ = _active_lesson_and_number(state)
    if lesson is None:
        return jsonify({
            "output": "Koniec kursu! Brak kolejnych zadań.",
            "success": True,
            "completed": True,
            "reload": False,
        })

    code = request.json.get('code', '')

    try:
        with tempfile.TemporaryDirectory() as workdir:
            temp_path = os.path.join(workdir, "student_code.py")
            with open(temp_path, "w", encoding="utf-8") as temp_file:
                temp_file.write(code)

            result = subprocess.run(
                [sys.executable, temp_path],
                capture_output=True,
                text=True,
                timeout=3,
                cwd=workdir,
            )

        output = result.stdout
        error = result.stderr

        full_output = output + error
        success = False

        if result.returncode == 0:
            if is_acceptable_output(lesson['expected_output'], output):
                success = True
                if state["test_mode"]:
                    full_output += "\n✅ Poprawna odpowiedź."
                else:
                    state["current_lesson_index"] += 1
                    full_output += "\n✅ ZADANIE WYKONANE PERFEKCYJNIE! Przechodzisz dalej..."
            else:
                full_output += (
                    "\n❌ Wynik jest niepoprawny.\n\n"
                    f"Twój kod wypluł: '{output.strip()}'\n"
                    f"Oczekiwaliśmy: '{lesson['expected_output'].strip()}'"
                )
        else:
            full_output += "\n❌ WYSTĄPIŁ BŁĄD W KODZIE PYTHONA (sprawdź linijki błędu wyżej)"

        if state["test_mode"]:
            section = _lesson_section(lesson)
            stats = state["test_section_stats"].setdefault(section, {"total": 0, "wrong": 0})
            stats["total"] += 1
            if not success:
                stats["wrong"] += 1

            state["test_results"].append({
                "lesson_id": lesson["id"],
                "section": section,
                "correct": success,
            })

            state["test_position"] += 1
            reload = True

            if state["test_position"] >= len(state["test_question_indices"]):
                full_output += "\n🏁 Test zakończony. Kliknij 'Zakończ test', aby wrócić do kursu i zobaczyć raport działów do powtórki."
            else:
                full_output += (
                    f"\n➡️ Przechodzimy do następnego pytania "
                    f"({state['test_position'] + 1}/{len(state['test_question_indices'])})."
                )
        else:
            reload = success

        _save_state(state)
        return jsonify({
            "output": full_output,
            "success": success,
            "reload": reload,
        })

    except subprocess.TimeoutExpired:
        return jsonify({
            "output": "❌ BŁĄD: Wykonywanie kodu trwało zbyt długo (masz nieskończoną pętlę?).",
            "success": False,
            "reload": False,
        })


@app.route('/start_random_test', methods=['POST'])
def start_random_test():
    state = _get_state()
    if state is None:
        return _unauthorized_json()

    question_count = min(TEST_SIZE, len(LESSONS))
    if question_count == 0:
        return jsonify({"success": False, "message": "Brak lekcji do testu."})

    _reset_test_state(state)
    state["test_question_indices"] = random.sample(range(len(LESSONS)), question_count)
    state["test_mode"] = True
    _save_state(state)
    return jsonify({"success": True, "reload": True})


@app.route('/end_random_test', methods=['POST'])
def end_random_test():
    state = _get_state()
    if state is None:
        return _unauthorized_json()

    _reset_test_state(state)
    _save_state(state)
    return jsonify({"success": True, "reload": True})


@app.route('/reset', methods=['POST'])
def reset():
    state = _get_state()
    if state is None:
        return _unauthorized_json()

    state["current_lesson_index"] = 0
    _reset_test_state(state)
    _save_state(state)
    return jsonify({"success": True})


if __name__ == '__main__':
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    print(f"Uruchamiam aplikację pod adresem: http://{host}:{port}")
    print("Wciśnij CTRL+C w terminalu, aby zatrzymać aplikację.")
    app.run(host=host, port=port, debug=debug)
