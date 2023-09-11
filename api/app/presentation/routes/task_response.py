from datetime import date
from pydantic import BaseModel

class TaskResponse(BaseModel):
    id: str
    title: str
    description: str
    date: date 
    completed: bool
    
    class Config:
        arbitrary_types_allowed = True
