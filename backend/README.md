# Kortix MVP - Backend

FastAPI-based backend for the Kortix AI Agent Platform.

## Setup

### 1. Install Dependencies

```bash
pip install uv
uv sync
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your credentials
```

### 3. Run Development Server

```bash
uv run uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

### 4. Run Background Worker

```bash
uv run dramatiq --skip-logging --processes 2 --threads 4 run_agent_background
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

```bash
uv run pytest
```

## Docker

```bash
docker build -t kortix-backend .
docker run -p 8000:8000 --env-file .env kortix-backend
```
