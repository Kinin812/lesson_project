from django.db import models

class Lesson(models.Model):
    STATUS_CREATED = "created"
    STATUS_COMPLETED = "completed"

    STATUS_CHOICES = (
        (STATUS_CREATED, "Created"),
        (STATUS_COMPLETED, "Completed"),
    )

    title = models.CharField(max_length=255)
    student_id = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_CREATED,
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def complete(self):
        self.status = self.STATUS_COMPLETED
        self.save(update_fields=["status"])