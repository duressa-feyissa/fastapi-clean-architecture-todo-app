import datetime
import unittest
from unittest.mock import MagicMock
from app.domain.use_cases.view_tasks import ViewAllTasks
from app.domain.repositories.base_repository import BaseRepository
from app.domain.entities.task import TaskEntity, Task
from core.common.either import Either
from core.use_cases.use_case import NoParams
from core.errors.failure import Failure

class TestViewTasks(unittest.IsolatedAsyncioTestCase):
    
    def setUp(self) -> None:
        self.tTasks = [
            Task(
                id='1',
                title='title',
                description='description',
                date=datetime.datetime.now(),
                completed=True
            ),
            Task(
                id='2',
                title='title',
                description='description',
                date=datetime.datetime.now(),
                completed=True
            )
        ]
        self.repository = MagicMock(BaseRepository)
        self.use_case = ViewAllTasks(self.repository)
        
    async def test_view_tasks_success(self):
        mock_task = [TaskEntity.from_dict(task) for task in self.tTasks]
        params = NoParams()
        
        self.repository.view_tasks.return_value = Either.right(mock_task)
        
        result = await self.use_case(params)
        self.assertTrue(result.is_right())
        self.assertEqual(result.get(), mock_task)
        self.repository.view_tasks.assert_called_once_with()
        
    async def test_view_tasks_failure(self):
        params = NoParams()
        self.repository.view_tasks.return_value = Either.left(Failure())
        
        result = await self.use_case(params)
        self.assertTrue(result.is_left())
        self.assertEqual(result.get(), Failure())
        self.repository.view_tasks.assert_called_once_with()
