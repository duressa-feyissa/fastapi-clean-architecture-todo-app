import datetime
import unittest
from unittest.mock import MagicMock
from app.domain.use_cases.view_task import ViewTask, Params
from app.domain.repositories.base_repository import BaseRepository
from app.domain.entities.task import TaskEntity, Task
from core.common.either import Either
from core.errors.failure import Failure

class TestViewTask(unittest.IsolatedAsyncioTestCase):
        
        def setUp(self) -> None:
            self.tTask = Task(
                id='1',
                title='title',
                description='description',
                date=datetime.datetime.now(),
                completed=True
            )
            self.repository = MagicMock(BaseRepository)
            self.use_case = ViewTask(self.repository)
        
        async def test_view_task_success(self):    
            mock_task = TaskEntity.from_dict(self.tTask)
            params = Params(task_id=mock_task.id)
                
            self.repository.view_task.return_value = Either.right(mock_task)
                
            result = await self.use_case(params)
            self.assertTrue(result.is_right())
            self.assertEqual(result.get(), mock_task)
            self.repository.view_task.assert_called_once_with(mock_task.id)
            
        async def test_view_task_failure(self):
            mock_task = TaskEntity.from_dict(self.tTask)
            params = Params(task_id=mock_task.id)
                
            self.repository.view_task.return_value = Either.left(Failure())
                
            result = await self.use_case(params)
            self.assertTrue(result.is_left())
            self.assertEqual(result.get(), Failure())
            self.repository.view_task.assert_called_once_with(mock_task.id)