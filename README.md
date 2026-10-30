# jenkins-demo
A simple project to work with jenkins pipeline

A minimal FastAPI web application:

| Path       | Description                                              |
|------------|----------------------------------------------------------|
| `/`        | Modern welcome page showing the live current date & time |
| `/healthz` | Health check – returns `{"healthy": true}` with HTTP 200 |

## Project layout

```
app/
├── main.py              # FastAPI application
├── templates/index.html # welcome page
└── static/
    ├── css/style.css
    └── js/clock.js      # live clock
tests/test_main.py       # pytest tests
Dockerfile
```

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --host 0.0.0.0 --port 5000
```

## Test

```bash
pytest
```

## Docker

```bash
docker build -t jenkins-demo .
docker run --rm -p 5000:5000 jenkins-demo
curl http://localhost:5000/healthz
```

Open http://localhost:5000 in a browser.
