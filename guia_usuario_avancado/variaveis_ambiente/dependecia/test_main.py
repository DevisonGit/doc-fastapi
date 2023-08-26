from fastapi.testclient import TestClient
from config import Settings
from .main import app, get_settings

client = TestClient(app)


def get_settings_override():
    return Settings(admin_email="testing_admin@example.com")

app.dependency_overrides[get_settings] = get_settings_override


def test_app():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {
        "app_name": "Awesome API",
        "admin_email": "testing_admin@example.com",
        "items_per_user": 50,
    }