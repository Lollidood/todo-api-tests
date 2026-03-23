import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_todos():
    response = requests.get(f"{BASE_URL}/todos")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_todo():
    response = requests.get(f"{BASE_URL}/todos/1")
    
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_todo_completed_field():
    response = requests.get(f"{BASE_URL}/todos/1")
    data = response.json()
    
    assert "completed" in data
