from datetime import datetime

def format_deadline(deadline):
    # Форматирование даты и времени для красивого вывода
    return deadline.strftime('%d %B %Y, %H:%M')

def calculate_time_left(deadline, now=datetime.now()):
    # Расчет времени до наступления дедлайна
    delta = deadline - now
    days_left = delta.days
    hours_left = delta.seconds // 3600
    minutes_left = (delta.seconds // 60) % 60
    return days_left, hours_left, minutes_left
