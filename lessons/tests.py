from django.test import TestCase
from django.contrib.auth.models import User
from unittest.mock import patch
from lessons.models import Lesson
from lessons.tasks import send_lesson_notification

class LessonNotificationTests(TestCase):

    def setUp(self):
        """Подготовка данных перед каждым тестом"""
        self.student = User.objects.create_user(username='test_student', password='password')

    @patch('lessons.tasks.send_lesson_notification.delay')
    def test_lesson_creation_triggers_celery_task(self, mock_task_delay):
        """
        Тест 1: Проверяем, что при создании урока срабатывает сигнал
        и вызывается метод .delay() у задачи.
        """
        # 1. Создаем урок
        lesson = Lesson.objects.create(
            title="Intro to Testing",
            student_id=self.student.id
        )

        # 2. Проверяем, что задача была вызвана 1 раз
        self.assertTrue(mock_task_delay.called)
        self.assertEqual(mock_task_delay.call_count, 1)

        # 3. Проверяем, что в задачу передались правильные аргументы
        mock_task_delay.assert_called_with(
            student_id=self.student.id,
            lesson_title="Intro to Testing"
        )

    def test_celery_task_execution(self):
        """
        Тест 2: Проверяем, что код самой задачи работает без ошибок.
        """
        try:
            result = send_lesson_notification(
                student_id=self.student.id,
                lesson_title="Direct Test Lesson"
            )
            print(f"\nResult of task: {result}")

        except Exception as e:
            self.fail(f"Task raised an exception: {e}")

    @patch('lessons.tasks.send_lesson_notification.delay')
    def test_signal_does_not_trigger_on_update(self, mock_task_delay):
        """
        Тест 3: Проверяем, что уведомление НЕ отправляется при РЕДАКТИРОВАНИИ.
        """
        lesson = Lesson.objects.create(
            title="Old Title",
            student_id=self.student.id
        )
        mock_task_delay.reset_mock()

        # Меняем название и сохраняем
        lesson.title = "New Title"
        lesson.save()

        # Проверяем, что задача НЕ была вызвана повторно
        mock_task_delay.assert_not_called()