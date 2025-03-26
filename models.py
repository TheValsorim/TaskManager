from sqlalchemy import Column, Integer, String, Boolean
from database import Base  # Assuming 'Base' is defined in 'database.py'

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)

    __table_args__ = {'extend_existing': True}  # Add this line