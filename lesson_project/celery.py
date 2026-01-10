import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lesson_project.settings")

app = Celery("lesson_project", broker="redis://localhost:6379/0")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
