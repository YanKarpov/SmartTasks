from models.task_model import TaskModel

class TodoController:
    def __init__(self):
        self.task_model = TaskModel()
        self.load_tasks("tasks.json")
        self.task_model.update_task_statuses()

    def load_tasks(self, filename):
        self.task_model.load_tasks(filename)
        self.task_model.update_task_statuses()

    def save_tasks(self, filename):
        self.task_model.save_tasks(filename)

    def get_tasks(self):
        return self.task_model.get_tasks()









