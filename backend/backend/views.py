from datetime import datetime, timedelta

from django.shortcuts import render, redirect, get_object_or_404

from backend.models import Schedule
from backend.forms import ScheduleForm
from backend.utils import calculate_takings


def index(request):
    '''Главная страница.'''
    return render(request, 'index.html')


def create_schedule(request):
    '''Функция создания рецепта.'''
    user_id = request.GET.get('user_id')
    schedule_id = request.GET.get('schedule_id')
    if user_id and schedule_id:
        return redirect(
            f'/schedule/detail/?user_id={user_id}&schedule_id={schedule_id}'
        )
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save()
            return render(
                request,
                'backend/schedule_ok.html',
                {'schedule_id': schedule.id}
            )
    else:
        form = ScheduleForm()
    return render(request, 'backend/create_schedule.html', {'form': form})


def user_schedules(request):
    '''Функция обработки запросов расписания пользователя.'''
    user_id = request.GET.get('user_id')
    if not user_id:
        return render(
            request,
            'backend/error.html',
            {'error': 'Идентификатор пользователя (user_id) обязателен.'}
        )
    schedules = Schedule.objects.filter(user_id=user_id)
    if not schedules.exists():
        return render(
            request,
            'backend/error.html',
            {
                'error':
                '''Не найдено расписаний
                   для указанного идентификатора пользователя.'''
                }
        )
    return render(
        request,
        'backend/user_schedules.html',
        {'schedules': schedules, 'user_id': user_id}
    )


def schedule_detail(request):
    '''Функция просмотра отдельного рецепта.'''
    user_id = request.GET.get('user_id')
    schedule_id = request.GET.get('schedule_id')
    if not user_id or not schedule_id:
        return render(
            request,
            'error.html',
            {'error': '''Идентификатор пользователя (user_id)
                         и расписания (schedule_id) обязательны.'''}
        )
    schedule = get_object_or_404(Schedule, id=schedule_id, user_id=user_id)
    takings = calculate_takings(schedule)
    return render(
        request,
        'backend/schedule_detail.html',
        {'schedule': schedule, 'takings': takings}
    )


def next_takings(request):
    '''Функция просмотра расписания приема лекарств.'''
    user_id = request.GET.get('user_id')
    if not user_id:
        return render(
            request,
            'error.html',
            {'error': 'Идентификатор пользователя (user_id) обязателен.'}
        )
    schedules = Schedule.objects.filter(user_id=user_id)
    now = datetime.now()
    next_hour = now + timedelta(hours=1)
    takings = []
    for schedule in schedules:
        schedule_takings = calculate_takings(schedule)
        for time_str in schedule_takings:
            time_obj = datetime.strptime(time_str, "%H:%M").replace(
                year=now.year,
                month=now.month,
                day=now.day
            )
            if now <= time_obj <= next_hour:
                takings.append({
                    'medicament_name': schedule.medicament_name,
                    'time': time_str,
                })
    return render(
        request,
        'backend/next_takings.html',
        {'takings': takings, 'user_id': user_id}
    )
