from app.domain.repositories.base_repository import BaseRepository
from app.domain.entities.task import TaskEntity
from core.common.either import Either
from core.common.equatable import Equatable
from core.errors.failure import Failure
from core.use_cases.use_case import UseCase

class Params(Equatable):
    def __init__(self, task: TaskEntity) -> None:
        self.task = task
        
class CreateTask(UseCase[TaskEntity]):
    def __init__(self, repository: BaseRepository):
        self.repository = repository
    
    async def __call__(self, params: Params) -> Either[Failure, TaskEntity]:
        return await self.repository.create_task(params.task)