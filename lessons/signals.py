# lessons/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

from .models import Lesson
from .tasks import send_lesson_notification

@receiver(post_save, sender=Lesson)
def lesson_completed_handler(sender, instance: Lesson, created, **kwargs):
    if not created and instance.status == Lesson.STATUS_COMPLETED:
        transaction.on_commit(
            lambda: send_lesson_notification.delay(
                instance.student_id,
                instance.title,
            )
        )