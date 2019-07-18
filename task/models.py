from django.db import models
from base.models import AbstractDateTimeModel


class Task(AbstractDateTimeModel):
    assigned = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name = 'assigned', null=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name = 'created_by')
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    money = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.title
