import pytest
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_login_success(client):
    response = client.post('/login', data={"username": "admin", "password": "adminpass"})
    assert response.status_code in [200, 302]

def test_login_failure(client):
    response = client.post('/login', data={"username": "wrong", "password": "wrong"})
    assert response.status_code == 401

def test_logout(client):
    client.post('/login', data={"username": "admin", "password": "adminpass"})
    response = client.get('/logout')
    assert response.status_code in [200, 302]
