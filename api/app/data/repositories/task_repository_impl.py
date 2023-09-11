from app.domain.repositories.base_repository import BaseRepository
from app.data.datasources.task_local_datasource import TaskLocalDataSource
from core.errors.failure import Failure, CacheFailure
from core.errors.exceptions import CacheException
from core.common.either import Either
from app.domain.entities.task import TaskEntity

class TaskRepositoryImpl(BaseRepository):
        
        def __init__(self, task_local_datasource: TaskLocalDataSource):
            self.task_local_datasource = task_local_datasource
        
        async def create_task(self, task) -> Either[Failure, TaskEntity]:
            try:
                task = await self.task_local_datasource.create_task(task)
                return Either.right(task)
            except CacheException as e:
                return Either.left(CacheFailure(error_message=str(e)))
            
        async def update_task(self, task):
            try:
                task = await self.task_local_datasource.update_task(task)
                return Either.right(task)
            except CacheException as e:
                return Either.left(CacheFailure(error_message=str(e)))
        
        async def delete_task(self, task_id):
            try:
                task = await self.task_local_datasource.delete_task(task_id)
                return Either.right(task)
            except CacheException as e:
                return Either.left(CacheFailure(error_message=str(e)))
        
        async def view_tasks(self):
            try:
                tasks = await self.task_local_datasource.view_tasks()
                return Either.right(tasks)
            except CacheException as e:
                return Either.left(CacheFailure(error_message=str(e)))
        
        async def view_task(self, task_id):
            try:
                task = await self.task_local_datasource.view_task(task_id)
                return Either.right(task)
            except CacheException as e:
                return Either.left(CacheFailure(error_message=str(e)))

