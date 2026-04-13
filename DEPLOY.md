Jak uruchomic aplikacje online dla wielu uzytkownikow

1. Lokalny test produkcyjny
- cd ~/python-web-tutor
- /Users/zlotko25/miniforge3/bin/python -m pip install -r requirements.txt
- gunicorn --workers 4 --threads 8 --timeout 120 --bind 0.0.0.0:5000 app:app

2. Wdrozenie na Render (najprostsza opcja)
- Wrzuć katalog projektu do repozytorium GitHub.
- Na Render utwórz nowy Web Service z tego repo.
- Build Command: pip install -r requirements.txt
- Start Command: gunicorn --workers 4 --threads 8 --timeout 120 --bind 0.0.0.0:$PORT app:app
- Ustaw zmienne srodowiskowe:
  - APP_SECRET_KEY: losowy dlugi sekret
  - FLASK_DEBUG: 0

3. Co jest gotowe pod wielu uzytkownikow
- Postep kursu i stan testu sa trzymane per uzytkownik (sesja), nie globalnie.
- Aplikacja startuje na 0.0.0.0 i porcie z ENV.
- Dodany endpoint health: /health

4. Ważne ostrzezenie bezpieczenstwa
- Aplikacja wykonuje kod wpisany przez uzytkownika.
- Do publicznego ruchu zalecane jest uruchamianie wykonania kodu w izolacji (osobny kontener/sandbox, limity CPU/RAM, brak dostepu do hosta).
