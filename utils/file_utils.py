import json
from datetime import datetime
from tkinter import messagebox, filedialog

def load_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
            for task in tasks:
                if 'deadline' in task:
                    task['deadline'] = datetime.strptime(task['deadline'], '%Y-%m-%d %H:%M:%S')
    except FileNotFoundError:
        messagebox.showwarning("Предупреждение", "Файл задач не найден.")
    except json.JSONDecodeError:
        messagebox.showerror("Ошибка", "Ошибка при чтении файла задач.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при загрузке задач: {e}")
    return tasks

def save_tasks(tasks, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([{
                "task": task["task"],
                "deadline": task["deadline"].strftime('%Y-%m-%d %H:%M:%S') if isinstance(task["deadline"], datetime) else task["deadline"],
                "priority": task["priority"]
            } for task in tasks], file, indent=4, ensure_ascii=False)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при сохранении задач: {e}")

def load_tasks_dialog():
    filename = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    if filename:
        return load_tasks(filename)
    return []

def save_tasks_dialog(tasks):
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    if filename:
        save_tasks(tasks, filename)






