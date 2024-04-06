import sqlite3
import threading
from fastapi import FastAPI, HTTPException,Form
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI()

def get_sqlite_connection():
    if not hasattr(threading.current_thread(), "sqlite3_connection"):
        threading.current_thread().sqlite3_connection = sqlite3.connect('todo.db')
    return threading.current_thread().sqlite3_connection.cursor()

@app.get("/tasks")
def get_tasks():
    cursor = get_sqlite_connection()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    return {"tasks": tasks}

@app.post("/tasks")
def add_task(id: str = Form(), title: str = Form(), description: float = Form(), status: int = Form()):
    if status not in [0, 1]:
        return {"message": "Status must be either 0 or 1"}
    
    cursor = get_sqlite_connection()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('INSERT INTO tasks (id, title, description, time, status) VALUES (?, ?, ?, ?, ?)', (id, title, description, current_time, status))
    cursor.connection.commit()
    
    return {"message": "Task added successfully"}

@app.put("/tasks/{id}")
def update_task(id: int, title: str = Form(None), description: str = Form(None), time: str = Form(None), status: int = Form(None)):
    cursor = get_sqlite_connection()
    update_fields = []
    if title is not None:
        update_fields.append(f"title = '{title}'")
    if description is not None:
        update_fields.append(f"description = '{description}'")
    if time is not None:
        update_fields.append(f"time = '{time}'")
    if status is not None:
        update_fields.append(f"status = {status}")

    update_query = ', '.join(update_fields)
    cursor.execute(f'UPDATE tasks SET {update_query} WHERE id = ?', (id,))
    cursor.connection.commit()
    return {"message": "Task updated successfully"}

@app.delete("/tasks/{id}")
def delete_task(id: int):
    cursor = get_sqlite_connection()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
    cursor.connection.commit()
    return {"message": "Task deleted successfully"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

@app.on_event("shutdown")
def shutdown_event():
    if hasattr(threading.current_thread(), "sqlite3_connection"):
        threading.current_thread().sqlite3_connection.close()