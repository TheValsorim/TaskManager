from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate, TaskOut
from crud import get_task, get_tasks, create_task, update_task, delete_task
from database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks/", response_model=TaskOut)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db=db, task=task)

@router.get("/tasks/", response_model=list[TaskOut])
def get_tasks_endpoint(db: Session = Depends(get_db)):
    return get_tasks(db)

@router.get("/tasks/{task_id}", response_model=TaskOut)
def get_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=TaskOut)
def update_task_endpoint(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    updated_task = update_task(db=db, task_id=task_id, task=task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    success = delete_task(db=db, task_id=task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}
