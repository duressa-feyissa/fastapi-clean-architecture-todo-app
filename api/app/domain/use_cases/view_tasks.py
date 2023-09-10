from typing import Iterable
from app.domain.repositories.base_repository import BaseRepository
from app.domain.entities.task import TaskEntity
from core.common.either import Either
from core.errors.failure import Failure
from core.use_cases.use_case import UseCase, NoParams

class ViewAllTasks(UseCase[Iterable[TaskEntity]]):
    def __init__(self, repository: BaseRepository):
        self.repository = repository
    
    async def __call__(self, params: NoParams) -> Either[Failure, Iterable[TaskEntity]]:
        return await self.repository.view_tasks()
    

    

    
        


