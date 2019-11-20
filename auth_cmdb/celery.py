from __future__ import absolute_import,unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','auth_cmdb.settings')

app = Celery('auth_cmdb')

app.config_from_object('django.conf:settings',namespace='CELERY')

app.autodiscover_tasks()

# @app.task(bind=True)
# def dug_task(self):
#     print('Request: {0!r}'.format(self.request))