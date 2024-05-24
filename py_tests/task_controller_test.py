import pytest
from unittest.mock import MagicMock, patch
from controllers.task_controller import TaskController

@pytest.fixture
def task_controller():
    task_model_mock = MagicMock()
    master_mock = MagicMock()
    return TaskController(master_mock, task_model_mock)

@patch("controllers.task_controller.messagebox")
def test_add_task(messagebox_mock, task_controller):

    task_text = "Test Task"
    deadline = "2024-05-25"
    priority = "Высокий"
    

    task_controller.add_task(task_text, deadline, priority)
    

    task_controller.task_model.add_task.assert_called_once_with(task_text, deadline, priority)
    task_controller.task_model.update_task_statuses.assert_called_once()
    assert not messagebox_mock.showerror.called

@patch("controllers.task_controller.messagebox")
def test_edit_task(messagebox_mock, task_controller):

    task_text = "Edited Task"
    deadline = "2024-05-26"
    priority = "Средний"
    task_index = 1
    task_controller.get_selected_task_index = MagicMock(return_value=task_index)
    

    task_controller.edit_task(task_text, deadline, priority)
    

    task_controller.task_model.edit_task.assert_called_once_with(task_index, task_text, deadline, priority)
    task_controller.task_model.update_task_statuses.assert_called_once()
    assert not messagebox_mock.showerror.called

@patch("controllers.task_controller.messagebox")
def test_delete_task(messagebox_mock, task_controller):
    
    task_index = 2
    task_controller.get_selected_task_index = MagicMock(return_value=task_index)
    task_controller.task_model.delete_task = MagicMock()
    task_controller.master.update_tasks = MagicMock()
   
    task_controller.delete_task(task_index)
    
    task_controller.task_model.delete_task.assert_called_once_with(task_index)
    task_controller.master.update_tasks.assert_called_once()
    assert not messagebox_mock.showerror.called
