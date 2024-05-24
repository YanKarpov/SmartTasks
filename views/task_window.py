import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS, INFO
from tkinter import messagebox
from datetime import datetime

class TaskWindow(ttk.Toplevel):
    def __init__(self, master, task_controller, task_info=None):
        super().__init__(master)
        self.master = master
        self.task_controller = task_controller
        self.task_info = task_info
        
        if task_info:
            self.title("Редактировать задачу")
        else:
            self.title("Добавить задачу")
        
        self.geometry("600x300")
        self.create_widgets()
        
        # Обработчик закрытия окна
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        self.task_label = ttk.Label(self, text="Название задачи:", bootstyle=INFO)
        self.task_label.grid(row=0, column=0, padx=10, pady=5, sticky=ttk.W)
        
        self.task_entry = ttk.Entry(self, width=40)
        self.task_entry.grid(row=0, column=1, padx=10, pady=5, sticky=ttk.W)
        if self.task_info:
            self.task_entry.insert(ttk.END, self.task_info["task"])
        
        self.date_label = ttk.Label(self, text="Дата выполнения (гггг-мм-дд):", bootstyle=INFO)
        self.date_label.grid(row=1, column=0, padx=10, pady=5, sticky=ttk.W)
        
        self.date_entry = ttk.Entry(self, width=25)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5, sticky=ttk.W)
        if self.task_info:
            date_time = self.task_info["deadline"]
            self.date_entry.insert(ttk.END, date_time.strftime('%Y-%m-%d'))
        
        self.time_label = ttk.Label(self, text="Время выполнения (чч:мм):", bootstyle=INFO)
        self.time_label.grid(row=2, column=0, padx=10, pady=5, sticky=ttk.W)
        
        self.time_entry = ttk.Entry(self, width=25)
        self.time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=ttk.W)
        if self.task_info:
            date_time = self.task_info["deadline"]
            self.time_entry.insert(ttk.END, date_time.strftime('%H:%M'))
        
        self.priority_label = ttk.Label(self, text="Приоритет:", bootstyle=INFO)
        self.priority_label.grid(row=3, column=0, padx=10, pady=5, sticky=ttk.W)
        
        self.priority_combobox = ttk.Combobox(self, values=["Низкий", "Средний", "Высокий"])
        self.priority_combobox.grid(row=3, column=1, padx=10, pady=5, sticky=ttk.W)
        if self.task_info:
            self.priority_combobox.set(self.task_info["priority"])
        
        self.save_button = ttk.Button(self, text="Сохранить", command=self.save_task, bootstyle=SUCCESS)
        self.save_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    
    def save_task(self):
        new_task_text = self.task_entry.get()
        new_date_text = self.date_entry.get()
        new_time_text = self.time_entry.get()
        new_priority = self.priority_combobox.get()

        if new_task_text.strip() == "":
            messagebox.showerror("Ошибка", "Введите название задачи.")
            return

        if new_date_text.strip() == "" or new_time_text.strip() == "":
            messagebox.showerror("Ошибка", "Введите дату и время выполнения.")
            return

        try:
            deadline = datetime.strptime(f'{new_date_text} {new_time_text}', '%Y-%m-%d %H:%M')
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат даты и времени. Используйте форматы 'гггг-мм-дд' и 'чч:мм'.")
            return

        if self.task_info is not None and "index" in self.task_info:
            task_index = self.task_info["index"]
            self.task_controller.edit_task(task_index, new_task_text, deadline, new_priority)
        else:
            self.task_controller.add_task(new_task_text, deadline, new_priority)

        self.master.update_tasks()
        self.destroy()

    
    def on_close(self):
        # Освобождаем ссылку на окно задачи в главном приложении
        self.master.task_window = None
        self.destroy()

















   

    

    

    
