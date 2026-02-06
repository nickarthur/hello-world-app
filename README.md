# Hello World App

![Tests](https://github.com/nickarthur/hello-world-app/actions/workflows/tests.yml/badge.svg)

A Flask web app with several API endpoints.

## Setup

```bash
pyenv virtualenv 3.11.5 hello-world-app
pyenv local hello-world-app
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

The app runs at `http://127.0.0.1:5000`.

## Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Hello, World! page |
| `/greet/<name>` | GET | Personalized greeting |
| `/api/time` | GET | Current server timestamp |
| `/api/random?min=1&max=100` | GET | Random number generator |
| `/calculate/<op>/<a>/<b>` | GET | Calculator (add, subtract, multiply, divide) |
| `/api/echo` | POST | Echoes back JSON payload |

## Deploy

### Using Gunicorn

```bash
pip install gunicorn
gunicorn app:app
```

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn
COPY . .
EXPOSE 8000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
```

```bash
docker build -t hello-world-app .
docker run -p 8000:8000 hello-world-app
```

### Render / Railway

1. Push to GitHub
2. Connect the repo from the dashboard
3. Set the start command to `gunicorn app:app`
