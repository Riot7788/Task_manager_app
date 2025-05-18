from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Task

@shared_task
def check_upcoming_tasks():
    now = timezone.now()
    soon = now + timedelta(minutes=10)
    tasks = Task.objects.filter(
        status='undone',
        deadline__range=(now, soon)
    )

    for task in tasks:
        print(f"Задача скоро истечёт: {task.title} для пользователя {task.telegram_user_id}")