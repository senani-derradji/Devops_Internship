from fastapi.testclient import TestClient

from main import app


def test_root_returns_index():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello from FastAPI" in response.text
    assert "text/html" in response.headers.get("content-type", "")
