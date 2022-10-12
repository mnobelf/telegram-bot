# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY main.py main.py

COPY qa.sqlite3 qa.sqlite3

COPY .env .env

CMD [ "python3", "main.py", "--host=0.0.0.0"]