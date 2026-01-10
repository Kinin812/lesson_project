## Инфраструктура

Для упрощения локального запуска используется Docker Compose.

### Запуск инфраструктуры

docker-compose up -d

### Миграции

python manage.py migrate

### Celery worker

celery -A lesson_project worker -l info

### Django

python manage.py runserver