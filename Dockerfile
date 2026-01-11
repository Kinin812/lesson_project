FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi \
    && pip install uv

COPY . /app

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=lesson_project.settings

EXPOSE 8000