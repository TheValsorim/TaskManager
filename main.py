from fastapi import FastAPI, Depends
from routes import router
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Task, Base
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.include_router(router)
Base.metadata.create_all(bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Task Schema (for validation)
class TaskCreate(BaseModel):
    title: str
    completed: bool = False

class TaskResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True

# Create a task
@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(title=task.title, completed=task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get all tasks
@app.get("/tasks/", response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()
