from django.db import models
from base.models import AbstractDateTimeModel


class Task(AbstractDateTimeModel):
    assigned = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name = 'assigned')
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name = 'created_by')
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
