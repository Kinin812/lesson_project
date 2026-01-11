import logging
from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def send_lesson_notification(student_id: int, lesson_title: str):
    logger.info(
        "Уведомление отправлено студенту %s по уроку '%s'",
        student_id,
        lesson_title,
    )
