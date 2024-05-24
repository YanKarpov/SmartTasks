import pytest
from controllers.todo_controller import TodoController
from models.task_model import TaskModel
from datetime import datetime

@pytest.fixture
def task_controller():
    task_model = TaskModel()
    controller = TodoController()
    controller.task_model = task_model 
    return controller

def test_load_tasks(task_controller):
    task_controller.load_tasks("test_tasks.json") 
    
    loaded_tasks = task_controller.get_tasks()
    assert len(loaded_tasks) == 2
    assert loaded_tasks[0]["task"] == "Test Task 1"
    assert loaded_tasks[1]["task"] == "Test Task 2"


def test_update_task_statuses(task_controller):
    fixed_date = datetime.now()
    fixed_date.strftime('%Y-%m-%d %H:%M') 
    task_controller.task_model.tasks = [
        {"task": "Past Task", "deadline": "2022-01-01 12:00", "priority": "Низкий"},
        {"task": "Today Task", "deadline": fixed_date, "priority": "Средний"},
        {"task": "Future Task", "deadline": "2025-01-01 12:00", "priority": "Высокий"}
    ]
    
    task_controller.task_model.update_task_statuses()
    
    tasks = task_controller.get_tasks()
    assert tasks[0]["status"] == "Просрочено"
    assert tasks[1]["status"] == "Сегодня"
    assert tasks[2]["status"] == "Скоро"



