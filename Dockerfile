FROM python:3.12-slim

WORKDIR /app

COPY requarements.txt /

RUN pip install -r /requarements.txt --no-cache-dir

COPY . .
