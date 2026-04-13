Wdrozenie 24/7 na Azure for Students (Flask)

Status teraz
- Logowanie Azure CLI dziala.
- Konto studenckie jest poprawne, ale nie ma jeszcze aktywnej subskrypcji Azure.

Krok 1. Aktywuj Azure for Students
- Wejdz na: https://azure.microsoft.com/free/students/
- Zaloguj sie kontem: wojciech.zlotkowski@student.uj.edu.pl
- Dokoncz aktywacje oferty studenckiej.
- Potem sprawdz lokalnie:
  - az account list -o table

Krok 2. Deploy aplikacji (App Service)
- cd ~/python-web-tutor
- APP_NAME=python-web-tutor-$(date +%s)
- RG=python-web-tutor-rg
- PLAN=python-web-tutor-plan
- LOCATION=westeurope
- SECRET=$(/Users/zlotko25/miniforge3/bin/python - <<'PY'
import secrets
print(secrets.token_urlsafe(48))
PY
)

- az group create -n $RG -l $LOCATION
- az appservice plan create -n $PLAN -g $RG --is-linux --sku B1
- az webapp create -n $APP_NAME -g $RG -p $PLAN --runtime "PYTHON|3.12"
- az webapp config appsettings set -n $APP_NAME -g $RG --settings APP_SECRET_KEY="$SECRET" FLASK_DEBUG=0 SCM_DO_BUILD_DURING_DEPLOYMENT=true
- az webapp config set -n $APP_NAME -g $RG --startup-file "gunicorn --workers 2 --threads 4 --timeout 120 --bind 0.0.0.0:\$PORT app:app"
- zip -r deploy.zip . -x "*.git*" "__pycache__/*" "*.pyc"
- az webapp deploy -n $APP_NAME -g $RG --src-path deploy.zip --type zip
- az webapp show -n $APP_NAME -g $RG --query defaultHostName -o tsv

Krok 3. Sprawdzenie
- curl -I https://<host-z-poprzedniej-komendy>

Uwaga kosztowa
- Dla 24/7 uzywany jest plan B1 (nie Free F1), wiec schodzi z kredytu studenckiego.
