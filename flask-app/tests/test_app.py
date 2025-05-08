from app import app

def test_login():
    client = app.test_client()
    response = client.post('/login', data=dict(username="admin", password="password"))
    assert response.status_code in [200, 302]
