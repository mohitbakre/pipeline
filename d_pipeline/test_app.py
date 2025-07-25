# test_app.py
import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data


def test_health_check(client):
    response = client.get('/healthz')
    assert response.status_code == 200
    assert b'healthy' in response.data
