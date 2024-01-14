FROM python:3.11-buster

ENV PYTHONUNBUFFERED=1
ENV HOST=0.0.0.0
ENV PORT=8000

WORKDIR /code
COPY . /code/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD uvicorn webapp.main:app --host ${HOST} --port ${PORT}
