Task Manager API

A simple, yet powerful, Task Manager API built with FastAPI, SQLAlchemy, and Pydantic. This API allows users to manage tasks, including creating, retrieving, updating, and deleting tasks. Each task has a title, description, and completion status. It leverages SQLAlchemy for database management, FastAPI for fast API creation, and Pydantic for data validation.
Features

    Create tasks: Add new tasks with a title, description, and completion status.

    Read tasks: Retrieve all tasks or a specific task by its ID.

    Update tasks: Edit a task’s details, including its title, description, and completion status.

    Delete tasks: Remove tasks from the database.

    Dynamic ID generation: Task IDs are dynamically assigned and managed by the database.

Technologies Used

    FastAPI: A modern, fast web framework for building APIs with Python 3.6+.

    SQLAlchemy: A powerful ORM (Object-Relational Mapping) library for Python that provides a set of high-level API methods for interacting with relational databases.

    Pydantic: A data validation library that ensures the integrity of the input and output data.

    pytest: A testing framework for unit tests, ensuring API endpoints work correctly.

Endpoints
POST /tasks/

Create a new task.

    Request body:

{
  "title": "Task Title",
  "completed": false
}

Response:

    {
      "id": 1,
      "title": "Task Title",
      "completed": false
    }

GET /tasks/

Get a list of all tasks.

    Response:

    [
      {
        "id": 1,
        "title": "Task Title",
        "description": "Task Description",
        "completed": false
      },
      {
        "id": 2,
        "title": "Another Task",
        "completed": true
      }
    ]

GET /tasks/{task_id}

Get a specific task by ID.

    Response:

    {
      "id": 1,
      "title": "Task Title",
      "completed": false
    }

PUT /tasks/{task_id}

Update a specific task by ID.

    Request body:

{
  "title": "Updated Task Title",
  "completed": true
}

Response:

    {
      "id": 1,
      "title": "Updated Task Title",
      "completed": true
    }

DELETE /tasks/{task_id}

Delete a specific task by ID.

    Response:

    {
      "detail": "Task deleted"
    }

Installation

    Clone this repository:

git clone https://github.com/yourusername/task-manager-api.git

Navigate into the project directory:

cd task-manager-api

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate

Install the dependencies:

pip install -r requirements.txt

Run the application:

    uvicorn main:app --reload

Testing

To run the tests, use the following command:

pytest

This will run the test suite and ensure all API endpoints function as expected.
