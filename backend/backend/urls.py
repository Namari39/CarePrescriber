from django.contrib import admin
from django.urls import path

from backend import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('schedule/', views.create_schedule, name='create-schedule'),
    path('schedules/', views.user_schedules, name='user-schedules'),
    path('schedule/detail/', views.schedule_detail, name='schedule-detail'),
    path('next_takings/', views.next_takings, name='next-takings'),
]
