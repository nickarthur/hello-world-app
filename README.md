# Hello World App

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
