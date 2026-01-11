import logging
from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def send_lesson_notification(student_id: int, lesson_title: str):
    logger.info(f"Уведомление отправлено студенту {student_id} по уроку {lesson_title}")
