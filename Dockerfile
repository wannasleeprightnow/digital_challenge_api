FROM python:3.11

RUN mkdir /code

WORKDIR /code

COPY . .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements/dev.txt

WORKDIR src

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8080