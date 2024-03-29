FROM python:3.11-slim

WORKDIR /app

ENV LANG=C.UTF-8 \
  LC_ALL=C.UTF-8 \
  PATH="${PATH}:/root/.poetry/bin" \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONPATH=/app/hezar_api \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  TZ=Asia/Tehran

RUN apt update && apt upgrade -y && apt install curl -y && rm -rf /var/lib/apt/lists/*

# POETRY
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
  cd /usr/local/bin && \
  ln -s /opt/poetry/bin/poetry && \
  poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/
RUN poetry install -n --only main --no-root

COPY . /app

CMD uvicorn hezar_api.main:app --host 0.0.0.0 --port 80 --reload

