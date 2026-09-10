from fastapi.testclient import TestClient
from main import app
from database import SessionLocal
from models import Contact
from unittest.mock import MagicMock
from database import get_db
from main import create_app
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
            "budget": "Under $500",
            "project_type": "Website Development",
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
            "budget": "Under $500",
            "project_type": "Website Development",
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
            "budget": "Under $500",
            "project_type": "Website Development",
            "message": "Hi"
        }
    )

    assert response.status_code == 422

def test_create_contact_rejects_missing_name():
    response = client.post(
        "/contact",
        json={
            "email": "test@example.com",
            "budget": "Under $500",
            "project_type": "Website Development",
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
            "budget": "Under $500",
            "project_type": "Website Development",
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

def test_security_headers_are_present():
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
    assert response.headers["Referrer-Policy"] == "strict-origin-when-cross-origin"

def test_contact_database_error_is_hidden():
    fake_db = MagicMock()
    fake_db.commit.side_effect = Exception("SECRET DATABASE ERROR")

    def override_get_db():
        yield fake_db

    app.dependency_overrides[get_db] = override_get_db

    try:
        response = client.post(
            "/contact",
            json={
                "name": "Security Test",
                "email": "security@example.com",
                "budget": "Under $500",
                "project_type": "Website Development",
                "message": "This is a valid test contact message."
            }
        )

        assert response.status_code == 500
        assert response.json()["detail"] == "Unable to save contact message"
        assert "SECRET DATABASE ERROR" not in response.text
        fake_db.rollback.assert_called_once()

    finally:
        app.dependency_overrides.clear()

def test_docs_available_in_development():
    response = client.get("/docs")

    assert response.status_code == 200

def test_docs_hidden_in_production():
    class ProductionSettings:
        app_name = "Larbod"
        is_production = True

    production_app = create_app(ProductionSettings())
    production_client = TestClient(production_app)

    assert production_client.get("/docs").status_code == 404
    assert production_client.get("/redoc").status_code == 404
    assert production_client.get("/openapi.json").status_code == 404