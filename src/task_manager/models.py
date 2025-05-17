from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('undone', 'Undone'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    telegram_user_id = models.BigIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='undone')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
