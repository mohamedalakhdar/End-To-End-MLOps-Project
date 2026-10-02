# Stage 1: Builder
# =======================================================================
FROM python:3.13-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:0.12.17 /uv /uvx /usr/bin/

ENV UV_NO_CACHE=1\
    UV_PROJECT_ENVIRONMENT=/opt/venv

WORKDIR /build

COPY pyproject.toml uv.lock README.md ./

# Install production dependencies only
RUN uv sync --frozen --no-dev --no-default-groups --no-install-project 

COPY src ./src

# =======================================================================
# Stage 2: Runtime
# =======================================================================

FROM python:3.13-slim AS runtime

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/opt/venv/bin:$PATH"

COPY --from=builder /opt/venv /opt/venv

WORKDIR /app

COPY --from=builder /build/src ./src

RUN useradd --create-home --uid 1000 appuser

USER appuser

EXPOSE 8000

CMD ["uvicorn", "src.fraud_detection.fastapi_app.main:app", "--host", "0.0.0.0", "--port", "8000"]


