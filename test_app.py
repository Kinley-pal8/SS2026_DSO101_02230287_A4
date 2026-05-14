import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['message'] == "Welcome to the CI/CD Pipeline Demo"

def test_status(client):
    """Test the status endpoint"""
    response = client.get('/api/status')
    assert response.status_code == 200
    assert response.json['status'] == "Application is running"

def test_add(client):
    """Test the add endpoint with query parameters"""
    response = client.get('/api/add?a=5&b=3')
    assert response.status_code == 200
    assert response.json['result'] == 8

def test_add_negative(client):
    """Test add with negative numbers"""
    response = client.get('/api/add?a=-5&b=3')
    assert response.status_code == 200
    assert response.json['result'] == -2

def test_add_zero(client):
    """Test add with zero"""
    response = client.get('/api/add?a=0&b=0')
    assert response.status_code == 200
    assert response.json['result'] == 0

def test_add_path_version(client):
    """Test the add endpoint with path parameters (positive numbers)"""
    response = client.get('/api/add/10/5')
    assert response.status_code == 200
    assert response.json['result'] == 15

def test_1_plus_1():
    """Sample test from assignment"""
    assert 1 + 1 == 2
