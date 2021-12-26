import os
from celery import Celery
# Set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

app = Celery('app')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def add(self, x) -> int:
    return x ** 2


app.conf.beat_schedule = {
    'Send alarm notifications': {
        'task': '',
        'schedule': crontab()
    }
}
