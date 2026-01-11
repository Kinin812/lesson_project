from django.db.models.signals import post_save
from django.dispatch import receiver
from lessons.models import Lesson
from lessons.tasks import send_lesson_notification


@receiver(post_save, sender=Lesson)
def on_lesson_created(sender, instance, created, **kwargs):
    if created:
        send_lesson_notification.delay(
            student_id=instance.student_id, lesson_title=instance.title
        )
