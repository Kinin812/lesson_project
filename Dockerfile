FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml uv.lock* /app/

RUN pip install uv

COPY . /app

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=lesson_project.settings

EXPOSE 8000