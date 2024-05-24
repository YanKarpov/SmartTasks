from datetime import datetime
from tkinter import messagebox
from utils.file_utils import load_tasks, save_tasks

class TaskModel:
    def __init__(self):
        self.tasks = []

    def load_tasks(self, filename):
        self.tasks = load_tasks(filename)

    def save_tasks(self, filename):
        save_tasks(self.tasks, filename)

    def add_task(self, task_text, deadline, priority, status="active"):
        new_task = {
            "task": task_text,
            "deadline": deadline,
            "priority": priority,
            "status": status
        }
        self.tasks.append(new_task)

    def edit_task(self, task_index, task_text, deadline, priority, status="active"):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = {
                "task": task_text,
                "deadline": deadline,
                "priority": priority,
                "status": status
            }
        else:
            raise IndexError("Индекс задачи вне диапазона.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            raise IndexError("Индекс задачи вне диапазона.")

    def get_tasks(self):
        return self.tasks

    def update_task_statuses(self):
        now = datetime.now()
        for task in self.tasks:
            deadline = task["deadline"]
            if isinstance(deadline, str):
                # Конвертируем строку в datetime
                try:
                    deadline = datetime.strptime(deadline, '%Y-%m-%d %H:%M')
                    task["deadline"] = deadline
                except ValueError:
                    messagebox.showerror("Ошибка", f"Неверный формат даты для задачи: {task['task']}")
                    continue

            if deadline < now:
                task["status"] = "Просрочено"
            elif deadline.date() == now.date():
                task["status"] = "Сегодня"
            else:
                task["status"] = "Скоро"





    
