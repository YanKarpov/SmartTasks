from datetime import datetime
from utils.date_utils import format_deadline, calculate_time_left


def test_format_deadline():
    deadline = datetime(2024, 5, 20, 10, 30)  # Установим дедлайн
    formatted_deadline = format_deadline(deadline)
    expected_output = "20 May 2024, 10:30"  # Ожидаемый результат
    assert formatted_deadline == expected_output

def test_calculate_time_left():
    now = datetime(2024, 5, 21, 13, 00)  # Текущая дата и время
    deadline = datetime(2024, 5, 22, 15, 30)  # Установим дедлайн
    expected_days = 1
    expected_hours = 2
    expected_minutes = 30
    days_left, hours_left, minutes_left = calculate_time_left(deadline, now)
    assert days_left == expected_days
    assert hours_left == expected_hours
    assert minutes_left == expected_minutes


