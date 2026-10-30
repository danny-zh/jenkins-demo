from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"healthy": True}


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Welcome" in response.text
    assert "/static/js/clock.js" in response.text


def test_static_assets():
    assert client.get("/static/css/style.css").status_code == 200
    assert client.get("/static/js/clock.js").status_code == 200
