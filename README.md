# digital_challege

# Запуск

dev
```bash
git clone https://github.com/wannasleeprightnow/digital_challege_api.git
cd digital_challege_api/
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements/dev.txt
cd src/
uvicorn main:app
```

prod
```bash
git clone https://github.com/wannasleeprightnow/digital_challege_api.git
cd digital_challege_api/
sudo docker build . -t digital_challenge_api:latest
sudo docker run -d -p 7777:8000 digital_challenge_api 
```