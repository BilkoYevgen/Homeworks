import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homework.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1') # Без цієї настройки celery повністю відмовляється працювати на моїй windows

app = Celery('homework')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    'print-user-count-every-minute': {
        'task': 'user.tasks.print_user_count',
        'schedule': 60.0,
        'args': (),
        'kwargs': {},
    },
}
