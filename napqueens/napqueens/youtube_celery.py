import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'napqueens.settings')

celery_app = Celery('napqueens', backend='rredis://localhost:6379', broker='redis://localhost:6379')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()