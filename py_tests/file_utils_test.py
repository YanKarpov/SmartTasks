import os
from datetime import datetime
import pytest
from utils.file_utils import load_tasks, save_tasks

@pytest.fixture
def sample_tasks():
    return [
        {"task": "Task 1", "deadline": datetime(2024, 5, 20, 10, 30), "priority": 1},
        {"task": "Task 2", "deadline": datetime(2024, 5, 21, 12, 0), "priority": 2},
        {"task": "Task 3", "deadline": datetime(2024, 5, 22, 14, 30), "priority": 3}
    ]

def test_save_and_load_tasks(tmpdir, sample_tasks):
    filename = os.path.join(tmpdir, "test_tasks.json")

    # Сохраняем образцовые задачи
    save_tasks(sample_tasks, filename)

    # Загружаем задачи из файла
    loaded_tasks = load_tasks(filename)

    # Проверяем, что загруженные задачи соответствуют образцовым
    assert len(loaded_tasks) == len(sample_tasks)
    for loaded_task, sample_task in zip(loaded_tasks, sample_tasks):
        assert loaded_task["task"] == sample_task["task"]
        assert loaded_task["deadline"] == sample_task["deadline"]
        assert loaded_task["priority"] == sample_task["priority"]







