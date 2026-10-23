
from fastapi import FastAPI

app = FastAPI(title="Task Manager API")

tasks = []

@app.get("/")
def home():
    return {"message": "Task Manager API is running"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return {"message": "Task created", "task": task}
