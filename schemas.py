from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    completed: Optional[bool] = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    id: int

class TaskOut(TaskBase):
    id: int

    class Config:
        orm_mode = True
