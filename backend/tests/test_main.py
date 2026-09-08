from fastapi.testclient import TestClient
from main import app
from database import SessionLocal
from models import Contact
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

def test_create_contact_rejects_invalid_email():
    response = client.post(
        "/contact",
        json={
            "name": "Test User",
            "email": "not-an-email",
            "budget": "1000-5000",
            "project_type": "website",
            "message": "This is an automated test contact message."
        }
    )

    assert response.status_code == 422

def test_create_contact_rejects_short_message():
    response = client.post(
        "/contact",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "budget": "1000-5000",
            "project_type": "website",
            "message": "Hi"
        }
    )

    assert response.status_code == 422

def test_create_contact_rejects_missing_name():
    response = client.post(
        "/contact",
        json={
            "email": "test@example.com",
            "budget": "1000-5000",
            "project_type": "website",
            "message": "This is an automated test contact message."
        }
    )

    assert response.status_code == 422

def test_contact_is_saved_to_test_database():
    response = client.post(
        "/contact",
        json={
            "name": "Database Test User",
            "email": "database-test@example.com",
            "budget": "1000-5000",
            "project_type": "website",
            "message": "This contact should be stored in the test database."
        }
    )

    assert response.status_code == 200

    db = SessionLocal()

    try:
        contact = (
            db.query(Contact)
            .filter(Contact.email == "database-test@example.com")
            .first()
        )

        assert contact is not None
        assert contact.name == "Database Test User"

    finally:
        db.close()