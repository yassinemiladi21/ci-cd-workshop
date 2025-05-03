import pytest
from app import app

@pytest.fixture
def client():
    # Creates a test client
    app.testing = True
    return app.test_client()

def test_home_status_code(client):
    result = client.get('/')
    # Check if status code is 200
    assert result.status_code == 200
