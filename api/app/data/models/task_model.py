from sqlalchemy import Column, String, Boolean, DATE
from core.config.database_config import Base


class TaskModel(Base):
    __tablename__ = 'tasks'

    id = Column(String(36), primary_key=True, index=True)
    title = Column(String(256), nullable=False)
    description = Column(String(1024), nullable=False)
    date = Column(DATE, nullable=False)
    completed = Column(Boolean, nullable=False)
    
    def __repr__(self):
        return f'<TaskModel(id={self.id}, title={self.title}>'


