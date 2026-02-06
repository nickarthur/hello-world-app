import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data


def test_greet(client):
    response = client.get("/greet/Alicia")
    assert response.status_code == 200
    assert b"Hello, Alicia!" in response.data


def test_time(client):
    response = client.get("/api/time")
    assert response.status_code == 200
    data = response.get_json()
    assert "timestamp" in data
    assert "timezone" in data


def test_random_default(client):
    response = client.get("/api/random")
    assert response.status_code == 200
    data = response.get_json()
    assert 1 <= data["number"] <= 100


def test_random_custom_range(client):
    response = client.get("/api/random?min=10&max=20")
    assert response.status_code == 200
    data = response.get_json()
    assert 10 <= data["number"] <= 20
    assert data["min"] == 10
    assert data["max"] == 20


def test_calculate_add(client):
    response = client.get("/calculate/add/5/3")
    assert response.status_code == 200
    assert response.get_json()["result"] == 8


def test_calculate_subtract(client):
    response = client.get("/calculate/subtract/10/4")
    assert response.status_code == 200
    assert response.get_json()["result"] == 6


def test_calculate_multiply(client):
    response = client.get("/calculate/multiply/3/7")
    assert response.status_code == 200
    assert response.get_json()["result"] == 21


def test_calculate_divide(client):
    response = client.get("/calculate/divide/10/4")
    assert response.status_code == 200
    assert response.get_json()["result"] == 2.5


def test_calculate_divide_by_zero(client):
    response = client.get("/calculate/divide/5/0")
    assert response.status_code == 200
    assert response.get_json()["result"] == "Error: Division by zero"


def test_calculate_invalid_operation(client):
    response = client.get("/calculate/modulo/5/3")
    assert response.status_code == 200
    assert response.get_json()["result"] == "Invalid operation"


def test_echo(client):
    response = client.post("/api/echo", json={"message": "hello"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["received"] == {"message": "hello"}
    assert "timestamp" in data
