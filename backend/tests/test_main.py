from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home_page():
    response = client.get("/")

    assert response.status_code == 200


def test_create_contact():
    response = client.post(
        "/contact",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "budget": "1000-5000",
            "project_type": "website",
            "message": "This is an automated test contact message."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Contact message saved successfully"
    assert "id" in data