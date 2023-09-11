from uuid import uuid4
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import AsyncIterable, List
from app.domain.entities.task import Task, TaskEntity
from core.errors.exceptions import CacheException
from app.data.models.task_model import TaskModel

class TaskLocalDataSource(ABC):
    
    @abstractmethod
    async def create_task(self, task: Task) -> TaskEntity:
        ...

    @abstractmethod
    async def update_task(self, task: Task) -> TaskEntity:
        ...
    
    @abstractmethod
    async def delete_task(self, task_id: str) -> TaskEntity:
        ...
        
    @abstractmethod
    async def view_tasks(self) -> List[TaskEntity]:
        ...
        
    @abstractmethod
    async def view_task(self, task_id: str) -> TaskEntity:
        ...
        
class TaskLocalDataSourceImpl(TaskLocalDataSource):
    
    def __init__(self, db: Session):
        self.db = db
        
    async def create_task(self, task: Task) -> TaskEntity:
        _task = self.db.query(TaskModel).filter(TaskModel.id == task['id']).first()
        if _task is not None:
            raise CacheException("Task already exists")
        task = TaskModel(
            id=str(uuid4()),
            title=task['title'],
            description=task['description'],
            date=task['date'],
            completed=task['completed']
        )
        self.db.add(task)
        self.db.commit()
        return TaskEntity(
            id=task.id,
            title=task.title,
            description=task.description,
            date=task.date,
            completed=task.completed
        )
    
    async def update_task(self, task: Task) -> TaskEntity:
        _task = self.db.query(TaskModel).filter(TaskModel.id ==task['id']).first()
        if _task is None:
            raise CacheException("Task not found")
        _task.title = task['title']
        _task.description = task['description']
        _task.date = task['date']
        _task.completed = task['completed']
        self.db.commit()
        return TaskEntity(
            id=_task.id,
            title=_task.title,
            description=_task.description,
            date=_task.date,
            completed=_task.completed
        )
    
    async def delete_task(self, task_id: str) -> TaskEntity:
        task = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if task is None:
            raise CacheException("Task not found")
        self.db.delete(task)
        self.db.commit()
        return TaskEntity(
            id=task.id,
            title=task.title,
            description=task.description,
            date=task.date,
            completed=task.completed
        )
    
    async def view_tasks(self) -> List[TaskEntity]:
        tasks = self.db.query(TaskModel).all()
        if tasks is None:
            raise CacheException("Tasks not found")
        return [
            TaskEntity(
                id=task.id,
                title=task.title,
                description=task.description,
                date=task.date,
                completed=task.completed
            ) for task in tasks
        ]
        
    async def view_task(self, task_id: str) -> TaskEntity:
        task = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if task is None:
            raise CacheException("Task not found")
        return TaskEntity(
            id=task.id,
            title=task.title,
            description=task.description,
            date=task.date,
            completed=task.completed
        )
