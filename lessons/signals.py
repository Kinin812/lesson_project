# lessons/signals.py
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from lessons.models import Lesson
from lessons.tasks import send_lesson_notification


@receiver(post_save, sender=Lesson)
def lesson_completed_handler(sender, instance: Lesson, created, **kwargs):
    if not created and instance.status == Lesson.STATUS_COMPLETED:
        transaction.on_commit(
            lambda: send_lesson_notification.delay(
                instance.student_id,
                instance.title,
            )
        )
