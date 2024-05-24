import ttkbootstrap as ttk
from tkinter import Menu, messagebox
from PIL import Image, ImageTk
from controllers.todo_controller import TodoController
from controllers.task_controller import TaskController
from views.task_window import TaskWindow
from models.task_model import TaskModel
from utils.date_utils import calculate_time_left, format_deadline
from utils.file_utils import load_tasks_dialog, save_tasks_dialog


class ToDoApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("SmartTasks")
        self.geometry("1200x800")

        self.task_model = TaskModel()
        self.todo_controller = TodoController()
        self.task_controller = TaskController(self.todo_controller, self)

        self.task_window = None  # Атрибут для хранения ссылки на окно задачи

        self.add_icon = ImageTk.PhotoImage(Image.open("icons/add.png"))
        self.edit_icon = ImageTk.PhotoImage(Image.open("icons/edit.png"))
        self.delete_icon = ImageTk.PhotoImage(Image.open("icons/delete.png"))
        self.load_icon = ImageTk.PhotoImage(Image.open("icons/load.png"))
        self.save_icon = ImageTk.PhotoImage(Image.open("icons/save.png"))

        self.create_widgets()
        self.create_buttons()
        self.update_tasks()
        self.create_menu()


    def create_menu(self):
        menu_bar = Menu(self)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Загрузить задачи", command=self.load_tasks)
        file_menu.add_command(label="Сохранить задачи", command=self.save_tasks)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.quit)
        menu_bar.add_cascade(label="Файл", menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="О программе", command=self.show_about_info)
        menu_bar.add_cascade(label="Справка", menu=help_menu)

        self.config(menu=menu_bar)


    def show_about_info(self):
        info = "SmartTasks\nВерсия 1.2\nАвтор: Ян Карпов"
        messagebox.showinfo("О программе", info)

    def create_widgets(self):
        self.task_list_frame = ttk.Frame(self)
        self.task_list_frame.pack(fill='both', expand=True, padx=20, pady=10)

        self.task_list = ttk.Treeview(self.task_list_frame, columns=("task", "deadline", "priority", "time_left", "status"), show='headings')
        self.task_list.heading("task", text="Задача")
        self.task_list.heading("deadline", text="Дедлайн")
        self.task_list.heading("priority", text="Приоритет")
        self.task_list.heading("time_left", text="Оставшееся время до дедлайна")
        self.task_list.heading("status", text="Статус")
        self.task_list.pack(fill='both', expand=True, side='left')

        self.scrollbar = ttk.Scrollbar(self.task_list_frame, orient="vertical", command=self.task_list.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.task_list.configure(yscrollcommand=self.scrollbar.set)

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(side='bottom', fill='y', padx=20, pady=10)

    def create_buttons(self):
        self.create_add_button()
        self.create_edit_button()
        self.create_delete_button()
        self.create_load_button()
        self.create_save_button()

    def create_add_button(self):
        self.add_button = ttk.Button(self.button_frame, image=self.add_icon, command=self.add_task, style="Toolbutton")
        self.add_button.pack(side="left", padx=5, pady=5)

    def create_edit_button(self):
        self.edit_button = ttk.Button(self.button_frame, image=self.edit_icon, command=self.edit_task, style="Toolbutton")
        self.edit_button.pack(side="left", padx=5, pady=5)

    def create_delete_button(self):
        self.delete_button = ttk.Button(self.button_frame, image=self.delete_icon, command=self.delete_task, style="Toolbutton")
        self.delete_button.pack(side="left", padx=5, pady=5)

    def create_load_button(self):
        self.load_button = ttk.Button(self.button_frame, image=self.load_icon, command=self.load_tasks, style="Toolbutton")
        self.load_button.pack(side="left", padx=5, pady=5)

    def create_save_button(self):
        self.save_button = ttk.Button(self.button_frame, image=self.save_icon, command=self.save_tasks, style="Toolbutton")
        self.save_button.pack(side="left", padx=5, pady=5)

    def add_task(self):
        if self.task_window is not None and self.task_window.winfo_exists():
            self.task_window.focus()  # Если окно уже существует, фокусируйтесь на нем
            return
        self.task_window = TaskWindow(self, self.task_controller)

    def edit_task(self):
        selected_item = self.task_list.selection()
        if selected_item:
            task_index = self.task_list.index(selected_item[0])
            task_info = self.todo_controller.get_tasks()[task_index]
            if self.task_window is not None and self.task_window.winfo_exists():
                self.task_window.focus()  # Если окно уже существует, фокусируйтесь на нем
                return
            self.task_window = TaskWindow(self, self.task_controller, task_info)

    def get_selected_task_index(self):
        selected_item = self.task_list.focus()
        if selected_item:
            return self.task_list.index(selected_item)
        return None

    def delete_task(self):
        self.task_controller.delete_task()


    def load_tasks(self):
        tasks = load_tasks_dialog()
        if tasks:
            self.todo_controller.task_model.tasks = tasks
            self.update_tasks()

    def save_tasks(self):
        save_tasks_dialog(self.todo_controller.get_tasks())
        messagebox.showinfo("Успех", "Задачи сохранены.")

    def update_tasks(self):
        self.todo_controller.task_model.update_task_statuses()
        if self.task_list:
            for i in self.task_list.get_children():
                self.task_list.delete(i)
            for task in self.todo_controller.get_tasks():
                deadline = task["deadline"]
                days_left, hours_left, minutes_left = calculate_time_left(deadline)
                time_left_str = f"{days_left} days, {hours_left} hours, {minutes_left} minutes"
                self.task_list.insert("", "end", values=(task["task"], format_deadline(task["deadline"]), task["priority"], time_left_str, task["status"]))
        else:
            print("task_list не был инициализирован правильно")










