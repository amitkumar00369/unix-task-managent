from celery import shared_task
from .models import Task
import time
@shared_task
def auto_complete_task(task_id):
    try:
        # time.sleep(5)
        task = Task.objects.get(id=task_id)
        task.status = 'completed'
        task.save()
    except Task.DoesNotExist:
        pass
