from flask import Flask, render_template, request, jsonify, session
import subprocess
from flask import Flask, render_template, request, jsonify, session
import subprocess
import tempfile
import os
import sys
import ast
import math
import random
import shlex

# Dodajemy folder do ścieżki, żeby zaimportować lekcje
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from lessons import LESSONS

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY", "super-secret-bioinfo-key")
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
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


def _default_user_state():
    return {
        "current_lesson_index": 0,
        "test_mode": False,
        "test_question_indices": [],
        "test_position": 0,
        "test_results": [],
        "test_section_stats": {},
    }


def _get_state():
    state = session.get("state")
    defaults = _default_user_state()

    if not isinstance(state, dict):
        state = defaults
    else:
        for key, default_value in defaults.items():
            if key not in state:
                state[key] = default_value

    session["state"] = state
    session.modified = True
    return state


def _save_state(state):
    session["state"] = state
    session.modified = True


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


def _lesson_for_view(lesson):
    # Poprawiamy widoczne literówki i styl poleceń bez zmiany logiki zadań.
    return {
        **lesson,
        "title": _clean_language(lesson.get("title", "")),
        "description": _clean_language(lesson.get("description", "")),
        "initial_code": _clean_language(lesson.get("initial_code", "")),
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
    # Ignorujemy puste linie, aby drobne różnice formatowania nie oblewały zadania.
    return [line.strip() for line in text.splitlines() if line.strip()]


def _parse_number(value):
    try:
        return float(value)
    except ValueError:
        return None


def _numbers_close(a, b):
    # Celowo bardziej elastycznie niż porównanie 1:1.
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
    # 1) Tolerancja dla samych liczb: 50 == 50.0
    expected_num = _parse_number(expected_line)
    actual_num = _parse_number(actual_line)
    if expected_num is not None and actual_num is not None:
        return _numbers_close(expected_num, actual_num)

    # 2) Tolerancja dla struktur literalnych, np. list
    try:
        expected_literal = ast.literal_eval(expected_line)
        actual_literal = ast.literal_eval(actual_line)
        return _compare_values(expected_literal, actual_literal)
    except (ValueError, SyntaxError):
        pass

    # 2b) Tolerancja dla komend shell z różnym quotingiem
    try:
        expected_cmd = shlex.split(expected_line)
        actual_cmd = shlex.split(actual_line)
        if expected_cmd == actual_cmd:
            return True
    except ValueError:
        pass

    # 3) Tolerancja dla wielokrotnych spacji
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

    # 3b) Tolerancja dla listy CSV bez znaczenia kolejności
    if "," in expected_line and "," in actual_line and "[" not in expected_line and "[" not in actual_line:
        expected_items = sorted(item.strip().lower() for item in expected_line.split(",") if item.strip())
        actual_items = sorted(item.strip().lower() for item in actual_line.split(",") if item.strip())
        if expected_items == actual_items:
            return True

    # 4) Domyślnie: porównanie po strip()
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


@app.route('/health')
def health():
    return jsonify({"status": "ok", "lessons": len(LESSONS)})


@app.route('/')
def index():
    state = _get_state()

    if state["test_mode"] and state["test_position"] >= len(state["test_question_indices"]):
        report_lesson = {
            "title": "Raport losowego testu 30 pytań",
            "description": _build_test_report(state),
            "initial_code": "# Kliknij 'Zakończ test', aby wrócić do kursu",
        }
        return render_template(
            'index.html',
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
            "initial_code": "print('Kurs ukończony pomyślnie!')"
        }
        return render_template(
            'index.html',
            lesson=_lesson_for_view(lesson),
            lesson_num=len(LESSONS),
            total=len(LESSONS),
            in_test_mode=False,
            test_finished=False,
        )

    return render_template(
        'index.html',
        lesson=_lesson_for_view(lesson),
        lesson_num=lesson_num,
        total=total,
        in_test_mode=state["test_mode"],
        test_finished=False,
    )


@app.route('/run', methods=['POST'])
def run_code():
    state = _get_state()
    lesson, _, _ = _active_lesson_and_number(state)
    if lesson is None:
        return jsonify({"output": "Koniec kursu! Brak kolejnych zadań.", "success": True, "completed": True, "reload": False})

    code = request.json.get('code', '')

    try:
        # Uruchamiamy kod ucznia w osobnym katalogu tymczasowym.
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
        reload = False

        if result.returncode == 0:
            if is_acceptable_output(lesson['expected_output'], output):
                success = True
                if state["test_mode"]:
                    full_output += "\n✅ Poprawna odpowiedź."
                else:
                    state["current_lesson_index"] += 1
                    full_output += "\n✅ ZADANIE WYKONANE PERFEKCYJNIE! Przechodzisz dalej..."
            else:
                full_output += f"\n❌ Wynik jest niepoprawny.\n\nTwój kod wypluł: '{output.strip()}'\nOczekiwaliśmy: '{lesson['expected_output'].strip()}'"
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
                full_output += f"\n➡️ Przechodzimy do następnego pytania ({state['test_position'] + 1}/{len(state['test_question_indices'])})."
        else:
            reload = success

        _save_state(state)
        return jsonify({
            "output": full_output,
            "success": success,
            "reload": reload
        })

    except subprocess.TimeoutExpired:
        return jsonify({"output": "❌ BŁĄD: Wykonywanie kodu trwało zbyt długo (masz nieskończoną pętlę?).", "success": False, "reload": False})


@app.route('/start_random_test', methods=['POST'])
def start_random_test():
    state = _get_state()
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
    _reset_test_state(state)
    _save_state(state)
    return jsonify({"success": True, "reload": True})


@app.route('/reset', methods=['POST'])
def reset():
    state = _get_state()
    state["current_lesson_index"] = 0
    _reset_test_state(state)
    _save_state(state)
    return jsonify({"success": True})


if __name__ == '__main__':
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    print(f"🚀 Uruchamiam aplikację pod adresem: http://{host}:{port}")
    print("Wciśnij CTRL+C w terminalu, aby zatrzymać aplikację.")
    app.run(host=host, port=port, debug=debug)
