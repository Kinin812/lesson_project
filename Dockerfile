FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./

ENV UV_PROJECT_ENVIRONMENT="/opt/venv"
ENV UV_COMPILE_BYTECODE="1"

RUN uv sync --frozen --no-dev

ENV PATH="/opt/venv/bin:$PATH"

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]