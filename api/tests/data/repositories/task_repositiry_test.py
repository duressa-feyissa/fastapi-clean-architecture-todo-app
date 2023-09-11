from unittest import mock
import unittest
from unittest.mock import AsyncMock
from app.data.datasources.task_local_datasource import TaskLocalDataSource
from app.data.repositories.task_repository_impl import TaskRepositoryImpl
from core.errors.exceptions import CacheException
from core.common.either import Either
from app.domain.entities.task import TaskEntity, Task
from core.errors.failure import CacheFailure

class TestTaskRepository(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.task_data = {
            'id': '1',
            'title': 'title',
            'description': 'description',
            'date': 'date',
            'completed': True
        }
        self.tTask = Task(**self.task_data)
        self.task_local_datasource = AsyncMock(spec=TaskLocalDataSource)
        self.repository = TaskRepositoryImpl(self.task_local_datasource)

    async def test_create_task_success(self):
        # Arrange
        expected_task = TaskEntity.from_dict(self.task_data)
        self.task_local_datasource.create_task.return_value = expected_task

        # Act
        result = await self.repository.create_task(self.tTask)

        # Assert
        self.assertIsInstance(result, Either)
        self.assertTrue(result.is_right())
        self.assertEqual(result.get(), expected_task)
        self.assertIsInstance(result.get(), TaskEntity)
        self.task_local_datasource.create_task.assert_called_once_with(self.tTask)

    async def test_create_task_failure(self):
        # Arrange
        self.task_local_datasource.create_task.side_effect = CacheException("Error")

        # Act
        result = await self.repository.create_task(self.tTask)

        # Assert
        self.assertIsInstance(result, Either)
        self.assertTrue(result.is_left())
        self.assertIsInstance(result.get(), CacheFailure)
        self.assertEqual(result.get().error_message, "Error")
        self.task_local_datasource.create_task.assert_called_once_with(self.tTask)


    async def test_update_task_success(self):
        # Arrange
        expected_task = TaskEntity.from_dict(self.task_data)
        self.task_local_datasource.update_task.return_value = expected_task

        # Act
        result = await self.repository.update_task(self.tTask)

        # Assert
        self.assertIsInstance(result, Either)
        self.assertTrue(result.is_right())
        self.assertEqual(result.get(), expected_task)
        self.assertIsInstance(result.get(), TaskEntity)
        self.task_local_datasource.update_task.assert_called_once_with(self.tTask)
        
    async def test_update_task_failure(self):
        # Arrange
        self.task_local_datasource.update_task.side_effect = CacheException("Error")

        # Act
        result = await self.repository.update_task(self.tTask)

        # Assert
        self.assertIsInstance(result, Either)
        self.assertTrue(result.is_left())
        self.assertIsInstance(result.get(), CacheFailure)
        self.assertEqual(result.get().error_message, "Error")
        self.task_local_datasource.update_task.assert_called_once_with(self.tTask)
        
    async def test_delete_task_success(self):
        # Arrange
        expected_task = TaskEntity.from_dict(self.task_data)
        self.task_local_datasource.delete_task.return_value = expected_task

        # Act
        result = await self.repository.delete_task(self.tTask["id"])

        # Assert
        self.assertIsInstance(result, Either)
        self.assertTrue(result.is_right())
        self.assertEqual(result.get(), expected_task)
        self.assertIsInstance(result.get(), TaskEntity)
        self.task_local_datasource.delete_task.assert_called_once_with(self.tTask["id"])
    
    async def test_delete_task_failure(self):
        # Arrange
        self.task_local_datasource.delete_task.side_effect = CacheException("Error")

        # Act
        result = await self.repository.delete_task(self.tTask["id"])

        # Assert
        self.assertIsInstance(result, Either)
        self.assertTrue(result.is_left())
        self.assertIsInstance(result.get(), CacheFailure)
        self.assertEqual(result.get().error_message, "Error")
        self.task_local_datasource.delete_task.assert_called_once_with(self.tTask["id"])
        
    async def test_view_tasks_success(self):
        # Arrange
        expected_task = TaskEntity.from_dict(self.task_data)
        self.task_local_datasource.view_tasks.return_value = [expected_task]

        # Act
        result = await self.repository.view_tasks()

        # Assert
        self.assertIsInstance(result, Either)
        self.assertTrue(result.is_right())
        self.assertEqual(result.get(), [expected_task])
        self.assertIsInstance(result.get(), list)
        self.assertIsInstance(result.get()[0], TaskEntity)
        self.task_local_datasource.view_tasks.assert_called_once()
        
    async def test_view_tasks_failure(self):
        # Arrange
        self.task_local_datasource.view_tasks.side_effect = CacheException("Error")

        # Act
        result = await self.repository.view_tasks()

        # Assert
        self.assertIsInstance(result, Either)
        self.assertTrue(result.is_left())
        self.assertIsInstance(result.get(), CacheFailure)
        self.assertEqual(result.get().error_message, "Error")
        self.task_local_datasource.view_tasks.assert_called_once()
        
    async def test_view_task_success(self):
        # Arrange
        expected_task = TaskEntity.from_dict(self.task_data)
        self.task_local_datasource.view_task.return_value = expected_task

        # Act
        result = await self.repository.view_task(self.tTask["id"])

        # Assert
        self.assertIsInstance(result, Either)
        self.assertTrue(result.is_right())
        self.assertEqual(result.get(), expected_task)
        self.assertIsInstance(result.get(), TaskEntity)
        self.task_local_datasource.view_task.assert_called_once_with(self.tTask["id"])
        
    async def test_view_task_failure(self):
        # Arrange
        self.task_local_datasource.view_task.side_effect = CacheException("Error")

        # Act
        result = await self.repository.view_task(self.tTask["id"])

        # Assert
        self.assertIsInstance(result, Either)
        self.assertTrue(result.is_left())
        self.assertIsInstance(result.get(), CacheFailure)
        self.assertEqual(result.get().error_message, "Error")
        self.task_local_datasource.view_task.assert_called_once_with(self.tTask["id"])
        