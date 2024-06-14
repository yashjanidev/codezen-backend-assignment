# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

# app = Celery('api')

# app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks()

# app.conf.timezone = 'UTC'

# app.conf.task_routes = {'api.product.tasks.*': {'queue': 'default'}}

# __all__ = ('app',)

# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = Celery('api')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
