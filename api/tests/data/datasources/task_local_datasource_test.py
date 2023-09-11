import unittest
from unittest import mock
from core.errors.exceptions import CacheException
from app.data.models.task_model import TaskModel
from app.data.datasources.task_local_datasource import TaskLocalDataSourceImpl

class TestTaskLocalDataSourceImpl(unittest.TestCase):

    def setUp(self):
        self.db = mock.MagicMock()
        self.datasource = TaskLocalDataSourceImpl(self.db)

    async def test_create_task_success(self):
        # Arrange
        task = TaskModel(id='1', title='title', description='description', date='date', completed=True)
        self.db.query.return_value.filter.return_value.first.return_value = None

        # Act
        result = await self.datasource.create_task(task)

        # Assert
        self.assertEqual(result, task)
        self.db.query.assert_called_once()
        self.db.query.return_value.filter.assert_called_once()
        self.db.query.return_value.filter.return_value.first.assert_called_once()
        self.db.add.assert_called_once()
        self.db.commit.assert_called_once()
    
    async def test_create_task_failure(self):
        # Arrange
        task = TaskModel(id='1', title='title', description='description', date='date', completed=True)
        self.db.query.return_value.filter.return_value.first.return_value = task

        # Act
        with self.assertRaises(CacheException):
            await self.datasource.create_task(task)

        # Assert
        self.db.query.assert_called_once()
        self.db.query.return_value.filter.assert_called_once()
        self.db.query.return_value.filter.return_value.first.assert_called_once()
        self.db.add.assert_not_called()
        self.db.commit.assert_not_called()
        
    async def test_update_task_success(self):
        # Arrange
        task = TaskModel(id='1', title='title', description='description', date='date', completed=True)
        self.db.query.return_value.filter.return_value.first.return_value = task

        # Act
        result = await self.datasource.update_task(task)

        # Assert
        self.assertEqual(result, task)
        self.db.query.assert_called_once()
        self.db.query.return_value.filter.assert_called_once()
        self.db.query.return_value.filter.return_value.first.assert_called_once()
        self.db.commit.assert_called_once()
        
    async def test_update_task_failure(self):
        # Arrange
        task = TaskModel(id='1', title='title', description='description', date='date', completed=True)
        self.db.query.return_value.filter.return_value.first.return_value = None

        # Act
        with self.assertRaises(CacheException):
            await self.datasource.update_task(task)

        # Assert
        self.db.query.assert_called_once()
        self.db.query.return_value.filter.assert_called_once()
        self.db.query.return_value.filter.return_value.first.assert_called_once()
        self.db.commit.assert_not_called()
        
    async def test_delete_task_success(self):
        # Arrange
        task = TaskModel(id='1', title='title', description='description', date='date', completed=True)
        self.db.query.return_value.filter.return_value.first.return_value = task

        # Act
        result = await self.datasource.delete_task(task.id)

        # Assert
        self.assertEqual(result, task)
        self.db.query.assert_called_once()
        self.db.query.return_value.filter.assert_called_once()
        self.db.query.return_value.filter.return_value.first.assert_called_once()
        self.db.delete.assert_called_once()
        self.db.commit.assert_called_once()
        
    async def test_delete_task_failure(self):
        # Arrange
        task = TaskModel(id='1', title='title', description='description', date='date', completed=True)
        self.db.query.return_value.filter.return_value.first.return_value = None

        # Act
        with self.assertRaises(CacheException):
            await self.datasource.delete_task(task.id)

        # Assert
        self.db.query.assert_called_once()
        self.db.query.return_value.filter.assert_called_once()
        self.db.query.return_value.filter.return_value.first.assert_called_once()
        self.db.delete.assert_not_called()
        self.db.commit.assert_not_called()
        
    async def test_view_tasks_success(self):
        # Arrange
        task = TaskModel(id='1', title='title', description='description', date='date', completed=True)
        self.db.query.return_value.all.return_value = [task]

        # Act
        result = await self.datasource.view_tasks()

        # Assert
        self.assertEqual(result, [task])
        self.db.query.assert_called_once()
        self.db.query.return_value.all.assert_called_once()
        
    async def test_view_task_success(self):
        # Arrange
        task = TaskModel(id='1', title='title', description='description', date='date', completed=True)
        self.db.query.return_value.filter.return_value.first.return_value = task

        # Act
        result = await self.datasource.view_task(task.id)

        # Assert
        self.assertEqual(result, task)
        self.db.query.assert_called_once()
        self.db.query.return_value.filter.assert_called_once()
        self.db.query.return_value.filter.return_value.first.assert_called_once()
    
    async def test_view_task_failure(self):
        # Arrange
        self.db.query.return_value.filter.return_value.first.return_value = None

        # Act
        with self.assertRaises(CacheException):
            await self.datasource.view_task('1')

        # Assert
        self.db.query.assert_called_once()
        self.db.query.return_value.filter.assert_called_once()
        self.db.query.return_value.filter.return_value.first.assert_called_once()
        