from core.common.either import Either
from core.errors.failure import Failure
from app.domain.entities.task import TaskEntity
from abc import ABC, abstractmethod
from typing import Iterable

class ContextManagerRepository(ABC):
    @abstractmethod
    def commit(self):
        ...

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.commit()


class BaseWriteOnlyRepository(ContextManagerRepository):
    @abstractmethod
    async def create_task(self, task: TaskEntity) -> Either[Failure, TaskEntity]:
        ...

    @abstractmethod
    async def update_task(self, task: TaskEntity) -> Either[Failure, TaskEntity]:
        ...

    @abstractmethod
    async def delete_task(self, task_id: str) -> Either[Failure, TaskEntity]:
        ...
    
class BaseReadOnlyRepository(ABC):
    @abstractmethod
    async def view_tasks(self) -> Either[Failure, Iterable[TaskEntity]]:
        ...

    @abstractmethod
    async def view_task(self, task_id: str) -> Either[Failure, TaskEntity]:
        ...


class BaseRepository(BaseReadOnlyRepository, BaseWriteOnlyRepository, ABC):
    ...
