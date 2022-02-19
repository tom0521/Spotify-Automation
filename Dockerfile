FROM python:3.8.10

COPY . /src

RUN pip install -r /src/requirements.txt