from tkinter import messagebox


class TaskController:
    def __init__(self, master, task_model):
        self.master = master
        self.task_model = task_model
        
    def add_task(self, task_text, deadline, priority):
        self.task_model.add_task(task_text, deadline, priority)
        self.task_model.update_task_statuses()

    def edit_task(self, task_text, deadline, priority):
        selected_index = self.get_selected_task_index()
        if selected_index is None:
            messagebox.showerror("Ошибка", "Выберите задачу для редактирования.")
            return
        self.task_model.edit_task(selected_index, task_text, deadline, priority)
        self.task_model.update_task_statuses()
        
    def delete_task(self, task_index):
        if task_index is None:
            messagebox.showerror("Ошибка", "Выберите задачу для удаления.")
            return
        confirm = messagebox.askyesno("Удаление задачи", "Вы уверены, что хотите удалить выбранную задачу?")
        if confirm:
            try:
                self.task_model.delete_task(task_index)
                self.master.update_tasks()
            except IndexError:
                messagebox.showerror("Ошибка", "Выбранная задача не найдена.")









