import pytest
from datetime import datetime, timedelta
from models.task_model import TaskModel

@pytest.fixture
def task_model():
    return TaskModel()

def test_add_task(task_model):
    task_model.add_task("Задача 1", datetime.now() + timedelta(days=1), "Высокий")
    tasks = task_model.get_tasks()
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Задача 1"
    assert tasks[0]["priority"] == "Высокий"

def test_add_multiple_tasks(task_model):
    task_model.add_task("Задача 1", datetime.now() + timedelta(days=1), "Высокий")
    task_model.add_task("Задача 2", datetime.now() + timedelta(days=2), "Средний")
    tasks = task_model.get_tasks()
    assert len(tasks) == 2
    assert tasks[0]["task"] == "Задача 1"
    assert tasks[1]["task"] == "Задача 2"

def test_edit_task(task_model):
    task_model.add_task("Задача 1", datetime.now() + timedelta(days=1), "Высокий")
    task_model.edit_task(0, "Отредактированная задача", datetime.now() + timedelta(days=2), "Низкий")
    tasks = task_model.get_tasks()
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Отредактированная задача"
    assert tasks[0]["priority"] == "Низкий"

def test_edit_task_invalid_index(task_model):
    task_model.add_task("Задача 1", datetime.now() + timedelta(days=1), "Высокий")
    with pytest.raises(IndexError):
        task_model.edit_task(1, "Отредактированная задача", datetime.now() + timedelta(days=2), "Низкий")

def test_delete_task(task_model):
    task_model.add_task("Задача 1", datetime.now() + timedelta(days=1), "Высокий")
    task_model.delete_task(0)
    tasks = task_model.get_tasks()
    assert len(tasks) == 0

def test_delete_task_invalid_index(task_model):
    task_model.add_task("Задача 1", datetime.now() + timedelta(days=1), "Высокий")
    with pytest.raises(IndexError):
        task_model.delete_task(1)

def test_update_task_statuses(task_model):
    # Создаем тестовые задачи с разными сроками выполнения
    now = datetime.now()
    past_deadline = now - timedelta(days=1)
    today_deadline = now
    future_deadline = now + timedelta(days=1)

    task_model.tasks = [
        {"task": "Задача 1", "deadline": past_deadline, "priority": "Высокий", "status": ""},
        {"task": "Задача 2", "deadline": today_deadline, "priority": "Средний", "status": ""},
        {"task": "Задача 3", "deadline": future_deadline, "priority": "Низкий", "status": ""}
    ]

    # Обновляем статусы задач
    task_model.update_task_statuses()

    # Проверяем, что статусы обновлены правильно
    assert task_model.tasks[0]["status"] == "Просрочено"
    assert task_model.tasks[1]["status"] == "Сегодня"
    assert task_model.tasks[2]["status"] == "Скоро"


