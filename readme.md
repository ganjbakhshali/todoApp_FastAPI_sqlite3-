# Todo App with FastAPI and SQLite

## Overview
This is a Todo application built with FastAPI and SQLite. It provides a simple API for managing tasks.

## Features
- CRUD operations for tasks (Create, Read, Update, Delete)
- SQLite database backend
- Error handling for HTTP exceptions

## Requirements
- Python 3.x
- FastAPI
- SQLite3

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
* Start the FastAPI server:
```
uvicorn sqlmain:app --reload
```
Access the API endpoints:
* View all tasks: http://localhost:8000/tasks [GET]
* Add a new task: http://localhost:8000/tasks [POST]
* Update a task: http://localhost:8000/tasks/{id} [PUT]
* Delete a task: http://localhost:8000/tasks/{id} [DELETE]

## API Documentation
You can access the Swagger UI documentation to explore and test the API endpoints:
http://localhost:8000/redoc

## Database
The application uses SQLite as the database backend. The database file todo.db will be created automatically.