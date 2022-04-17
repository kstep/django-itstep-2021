import os
from celery import Celery

app = Celery('hello')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello.settings')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
