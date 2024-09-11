from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_predict_success():
    response = client.post("/predict/", json={
        "title": "Fake News Title",
        "text": "This is a fake news article.",
        "subject": "politics",
        "date": "2022-01-01"
    })
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_missing_fields():
    response = client.post("/predict/", json={
        "title": "Fake News Title"
    })
    assert response.status_code == 422
