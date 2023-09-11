from fastapi import HTTPException, APIRouter, Depends
from typing import List

from app.data.datasources.task_local_datasource import TaskLocalDataSourceImpl
from app.domain.entities.task import Task
from app.domain.repositories.base_repository import BaseRepository as TaskRepository
from app.presentation.routes.task_response import TaskResponse
from app.domain.use_cases.create_task import CreateTask, Params as CreateTaskParams
from app.domain.use_cases.update_task import UpdateTask, Params as UpdateTaskParams
from app.domain.use_cases.delete_task import DeleteTask, Params as DeleteTaskParams
from app.domain.use_cases.view_task import ViewTask, Params as ViewTaskParams
from app.domain.use_cases.view_tasks import ViewAllTasks, NoParams
from app.data.repositories.task_repository_impl import TaskRepositoryImpl  
from core.config.database_config import get_db
from sqlalchemy.orm.session import Session

router = APIRouter()

def get_repository(db: Session = Depends(get_db)):
    task_local_datasource = TaskLocalDataSourceImpl(db=db)
    return TaskRepositoryImpl(task_local_datasource)

@router.post("/tasks/", response_model=TaskResponse)
async def create_task(
    task: Task,
    repository: TaskRepository = Depends(get_repository)
):
    create_task_use_case = CreateTask(repository)
    params = CreateTaskParams(task=task)
    result = await create_task_use_case(params)
    if result.is_right():
        return result.get()
    else:
        raise HTTPException(status_code=400, detail=result.get().error_message)

@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: str,
    task: Task,
    repository: TaskRepository = Depends(get_repository) 
):
    update_task_use_case = UpdateTask(repository)
    task['id'] = task_id
    params = UpdateTaskParams(task=task)
    result = await update_task_use_case(params)
    if result.is_right():
        return result.get()
    else:
        raise HTTPException(status_code=400, detail=result.get().error_message)

@router.delete("/tasks/{task_id}", response_model=TaskResponse)
async def delete_task(
    task_id: str,
    repository: TaskRepository = Depends(get_repository) 
):
    delete_task_use_case = DeleteTask(repository)
    params = DeleteTaskParams(task_id=task_id)
    result = await delete_task_use_case(params)
    if result.is_right():
        return result.get()
    else:
        raise HTTPException(status_code=400, detail=result.get().error_message)

@router.get("/tasks/", response_model=List[TaskResponse])
async def view_all_tasks(
    repository: TaskRepository = Depends(get_repository) 
):
    view_all_tasks_use_case = ViewAllTasks(repository)
    params = NoParams()
    result = await view_all_tasks_use_case(params)
    if result.is_right():
        return result.get()
    else:
        raise HTTPException(status_code=400, detail=result.get().error_message)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def view_task(
    task_id: str,
    repository: TaskRepository = Depends(get_repository)
):
    view_task_use_case = ViewTask(repository)
    params = ViewTaskParams(task_id=task_id)
    result = await view_task_use_case(params)
    if result.is_right():
        return result.get()
    else:
        raise HTTPException(status_code=404, detail=result.get().error_message)
