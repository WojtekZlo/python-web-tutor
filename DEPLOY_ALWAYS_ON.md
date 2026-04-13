Stale dzialajacy darmowy serwer (24/7) - najprostsza realna opcja

Dlaczego nie Render Free
- Render Free usypia aplikacje po braku ruchu, wiec nie jest to pelne 24/7.

Opcja 24/7 za 0 zl: Oracle Cloud Always Free (VM)
- To jest darmowa maszyna wirtualna, na ktorej Twoj kontener moze dzialac bez usypiania.
- Potrzebne konto Oracle (zwykle z weryfikacja karty).

1. Przygotuj repo
- Wrzuc ten projekt do GitHub.

2. Na Oracle utworz VM (Ubuntu)
- Otworz porty w Security List lub NSG: 80 i 443.
- Polacz sie przez SSH do VM.

3. Zainstaluj Docker na VM
- sudo apt update
- sudo apt install -y docker.io
- sudo systemctl enable --now docker
- sudo usermod -aG docker $USER
- wyloguj i zaloguj sie ponownie

4. Uruchom aplikacje
- git clone <adres-twojego-repo>
- cd python-web-tutor
- docker build -t python-web-tutor .
- docker run -d --name tutor --restart unless-stopped -p 80:8080 -e APP_SECRET_KEY="USTAW_DLUGI_SEKRET" python-web-tutor

5. Test
- curl -I http://IP_TWOJEJ_MASZYNY

6. HTTPS (zalecane)
- Najprosciej przez Cloudflare proxy (domena) albo reverse proxy z certbot na VM.

Wazne bezpieczenstwo
- Aplikacja wykonuje kod wpisany przez uzytkownika.
- Dla publicznego ruchu zalecana izolacja uruchomien (osobny worker/sandbox, limity CPU/RAM).
