FROM python:3.9-slim-buster

WORKDIR /

COPY . .

CMD ["python","bowling.py"]