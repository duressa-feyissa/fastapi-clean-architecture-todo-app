import unittest
from unittest.mock import MagicMock
from fastapi import HTTPException
from core.errors.exceptions import CacheException
from app.presentation.routes.tasks import create_task, view_all_tasks, view_task, update_task, delete_task

class TestCreateTask(unittest.TestCase):

    async def test_create_task_success(self):
        # Arrange
        task = {"title": "title", "description": "description", "date": "date", "completed": True, "id": "1"}
        repository = MagicMock()
        repository.create_task.return_value = task

        # Act
        result = await create_task(task, repository)

        # Assert
        self.assertEqual(result, task)
        repository.create_task.assert_called_once_with(task)
        
    async def test_create_task_fail(self):
        # Arrange
        task = {"title": "title", "description": "description", "date": "date", "completed": True, "id": "1"}
        repository = MagicMock()
        repository.create_task.side_effect = CacheException()

        # Act
        with self.assertRaises(HTTPException):
            await create_task(task, repository)

        # Assert
        repository.create_task.assert_called_once_with(task)
        
class TestViewAllTasks(unittest.TestCase):
    async def test_view_all_tasks_success(self):
        # Arrange
        repository = MagicMock()
        repository.view_all_tasks.return_value = []

        # Act
        result = await view_all_tasks(repository)

        # Assert
        self.assertEqual(result, [])
        repository.view_all_tasks.assert_called_once_with()
    
    async def test_view_all_tasks_fail(self):
        # Arrange
        repository = MagicMock()
        repository.view_all_tasks.side_effect = CacheException()

        # Act
        with self.assertRaises(HTTPException):
            await view_all_tasks(repository)

        # Assert
        repository.view_all_tasks.assert_called_once_with()

class TestViewTask(unittest.TestCase):
    async def test_view_task_success(self):
        # Arrange
        task_id = "1"
        task = {"title": "title", "description": "description", "date": "date", "completed": True, "id": "1"}
        repository = MagicMock()
        repository.view_task.return_value = task

        # Act
        result = await view_task(task_id, repository)

        # Assert
        self.assertEqual(result, task)
        repository.view_task.assert_called_once_with(task_id)
    
    async def test_view_task_fail(self):
        # Arrange
        task_id = "1"
        repository = MagicMock()
        repository.view_task.side_effect = CacheException()

        # Act
        with self.assertRaises(HTTPException):
            await view_task(task_id, repository)

        # Assert
        repository.view_task.assert_called_once_with(task_id)

class TestUpdateTask(unittest.TestCase):
    async def test_update_task_success(self):
        # Arrange
        task_id = "1"
        task = {"title": "title", "description": "description", "date": "date", "completed": True, "id": "1"}
        repository = MagicMock()
        repository.update_task.return_value = task

        # Act
        result = await update_task(task_id, task, repository)

        # Assert
        self.assertEqual(result, task)
        repository.update_task.assert_called_once_with(task_id, task)
    
    async def test_update_task_fail(self):
        # Arrange
        task_id = "1"
        task = {"title": "title", "description": "description", "date": "date", "completed": True, "id": "1"}
        repository = MagicMock()
        repository.update_task.side_effect = CacheException()

        # Act
        with self.assertRaises(HTTPException):
            await update_task(task_id, task, repository)

        # Assert
        repository.update_task.assert_called_once_with(task_id, task)
        
class TestDeleteTask(unittest.TestCase):
    async def test_delete_task_success(self):
        # Arrange
        task_id = "1"
        task = {"title": "title", "description": "description", "date": "date", "completed": True, "id": "1"}
        repository = MagicMock()
        repository.delete_task.return_value = task

        # Act
        result = await delete_task(task_id, repository)

        # Assert
        self.assertEqual(result, task)
        repository.delete_task.assert_called_once_with(task_id)
    
    async def test_delete_task_fail(self):
        # Arrange
        task_id = "1"
        repository = MagicMock()
        repository.delete_task.side_effect = CacheException()

        # Act
        with self.assertRaises(HTTPException):
            await delete_task(task_id, repository)

        # Assert
        repository.delete_task.assert_called_once_with(task_id)
        