from dataclasses import dataclass
import datetime
from typing import Optional, TypedDict
from app.domain.entities import BaseEntity

class Task(TypedDict):
    id: Optional[str]
    title: str
    description: str
    date: datetime.datetime
    completed: bool

@dataclass
class TaskEntity(BaseEntity):
    id: str
    title: str
    description: str
    date: datetime.datetime
    completed: bool
        
    @classmethod
    def from_dict(cls, other: Task) -> 'TaskEntity':
        return cls(
            id=other.get('id'),
            title=other['title'],
            description=other['description'],
            date=other['date'],
            completed=other['completed']
        )
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date': self.date,
            'completed': self.completed
        }
