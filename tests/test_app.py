import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"An error occurred while loading the index page" not in response.data

def test_recommend_ui(client):
    response = client.get('/recommend')
    assert response.status_code == 200
    assert b"An error occurred while loading the recommend page" not in response.data

def test_recommend_movies(client):
    response = client.post('/recommend_movies', data={'user_input': 'Some Movie'})
    assert response.status_code == 200
    assert b"An error occurred while processing the recommendation" not in response.data
