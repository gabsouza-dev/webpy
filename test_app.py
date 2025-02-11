from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'Bem-vindo' in response.data

def test_about():
    response = app.test_client().get('/sobre')
    assert response.status_code == 200
    assert b'Sobre' in response.data