from datetime import timedelta

from backend.constants import START_TIME, END_TIME, TIME_ALIGNMENT_INTERVAL


def calculate_takings(schedule):
    '''Функция для расчета времени приема лекарств.'''
    takings = []
    frequency = schedule.frequency
    if frequency == 1:
        takings.append(START_TIME.strftime("%H:%M"))
        return takings
    takings.append(START_TIME.strftime("%H:%M"))
    if frequency == 2:
        takings.append(END_TIME.strftime("%H:%M"))
        return takings
    total_minutes = (END_TIME - START_TIME).total_seconds() // 60
    interval_minutes = total_minutes / (frequency - 1)
    current_time = START_TIME
    for iteration in range(frequency - 2):
        current_time += timedelta(minutes=interval_minutes)
        rounded_time = round_time(current_time)
        takings.append(rounded_time.strftime("%H:%M"))
    takings.append(END_TIME.strftime("%H:%M"))
    return takings


def round_time(time):
    '''Округляет время в большую сторону до ближайших 15 минут.'''
    if time.minute % TIME_ALIGNMENT_INTERVAL == 0:
        return time
    add_minutes = TIME_ALIGNMENT_INTERVAL - (
        time.minute % TIME_ALIGNMENT_INTERVAL
    )
    return time + timedelta(minutes=add_minutes)
