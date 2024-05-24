# SmartTasks

## Описание
**SmartTasks** - это приложение "Напоминалка ака ToDo", созданное в рамках обучения по дисциплине «Язык программирования Python». Программа отображает список будущих событий и сообщает вам, сколько дней осталось до каждого из них. При повторном запуске через день время до дедлайна уменьшается, и программа отображает его в формате "дней до". Текущие, будущие и просроченные задачи выделены разными цветами.

### Основные функции
- **Добавление задач**
- **Редактирование задач**
- **Удаление задач**
- **Сохранение задач в новый JSON-файл**
- **Загрузка задач из другого JSON-файла**

### Формат хранения задач
Задачи хранятся в файле формата JSON с ключами:
- `task` (название задачи)
- `deadline` (срок выполнения, в формате YY-MM-DD H:M:S)
- `priority` (приоритет задачи)

### Архитектура
Проект реализован с использованием архитектурного паттерна **MVC (Model-View-Controller)**:
- **Model**: Управление данными и бизнес-логикой
- **View**: Представление пользовательского интерфейса (основано на библиотеке Tkinter)
- **Controller**: Управление взаимодействием между моделью и представлением

### Компиляция
Проект был скомпилирован в исполняемый файл `SmartTasks.exe` для удобного запуска.

### Тестирование
Проект прошел серию тестов для проверки функционала.

## Запуск приложения

### Основной функционал
Для оценки основного функционала используйте исполняемый файл:
SmartTasks.exe

### Расширенный функционал
Для рабочего тестирования, сохранения и загрузки задач запустите версию через:
main.py


## Известные баги и недоработки
- Версия приложения, скомпилированная в `SmartTasks.exe`, и версия, представленная в `.py` файлах, могут отличаться.
- Изменения затронули следующие файлы: `task_controller.py`, `todo_controller.py`, `task_window.py`, `todo_app.py`.
- Возможны ошибки в передаче атрибутов/индексов, из-за чего создание, редактирование и удаление задач могут не работать в версии, запускаемой через `main.py`. Рекомендуется использовать `SmartTasks.exe` для оценки работы основного функционала.
- 
