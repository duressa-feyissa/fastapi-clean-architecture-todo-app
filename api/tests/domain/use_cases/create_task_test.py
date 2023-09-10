import unittest
from unittest.mock import MagicMock
from app.domain.use_cases.create_task import CreateTask, Params
from app.domain.repositories.base_repository import BaseRepository
from app.domain.entities.task import TaskEntity, Task
from core.common.either import Either
from core.errors.failure import Failure

class TestCreateTask(unittest.IsolatedAsyncioTestCase):
    
    def setUp(self) -> None:
        self.tTask = Task(
            id='1',
            title='title',
            description='description',
            date='date',
            completed=True
        )
        self.repository = MagicMock(BaseRepository)
        self.use_case = CreateTask(self.repository)
      
    async def test_create_task_success(self):
        
        mock_task = TaskEntity.from_dict(self.tTask)
        params = Params(task=mock_task)
        
        self.repository.create_task.return_value = Either.right(mock_task)
        
        result = await self.use_case(params)
        self.assertTrue(result.is_right())
        self.assertEqual(result.get(), mock_task)
        self.repository.create_task.assert_called_once_with(mock_task)
        
    async def test_create_task_failure(self):
        mock_task = TaskEntity.from_dict(self.tTask)
        params = Params(task=mock_task)
        
        self.repository.create_task.return_value = Either.left(Failure())
        
        result = await self.use_case(params)
        self.assertTrue(result.is_left())
        self.assertEqual(result.get(), Failure())
        self.repository.create_task.assert_called_once_with(mock_task)
