FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install openssh-client vim flake8 nano

WORKDIR /djcrm

COPY . .

RUN pip install -r requiremets.txt