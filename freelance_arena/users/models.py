from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    CUSTOMER = 1
    EXECUTOR = 2

    USER_TYPE = (
        (CUSTOMER, _('CUSTOMER')),
        (EXECUTOR, _('EXECUTOR'))
    )
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE, default=EXECUTOR)
    # balance = 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
