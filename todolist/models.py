from django.db import models
from django.utils import timezone

class Task(models.Model):
    text = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    submission_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
