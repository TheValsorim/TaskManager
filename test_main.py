from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app from the main module
from database import SessionLocal
from models import Task

client = TestClient(app)


def test_create_task():
    # Create a task via the API
    response = client.post("/tasks/", json={"title": "Test Task", "description": "This is a test"})

    # Assert the response status code is 200 OK
    assert response.status_code == 200

    # Get the response data
    response_data = response.json()

    # Check that the ID exists in the response
    assert "id" in response_data
    task_id = response_data["id"]

    # Check the other fields
    assert response_data["title"] == "Test Task"
    assert response_data["completed"] is False  # Assuming default value for 'completed' is False

    # Now, fetch the task directly from the database to verify the creation
    db = SessionLocal()
    task_from_db = db.query(Task).filter(Task.id == task_id).first()
    db.close()

    # Verify that the task in the database matches the expected values
    assert task_from_db is not None  # Ensure the task exists in the database
    assert task_from_db.title == "Test Task"
    assert task_from_db.completed is False
