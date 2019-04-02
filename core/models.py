from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(blank=True, max_length=30, default="")
    last_name = models.CharField(blank=True, max_length=30, default="")
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def date(self):
        return self.registration_date.strftime('%d/%m/%Y')

    @property
    def time(self):
        return self.registration_date.strftime('%H:%M:%S')

    @property
    def username_refined(self):
        return self.username.replace("@", "-")

    @property
    def is_admin(self):
        if self.is_superuser == 1:
            return True
        return False

# class Group(models.Model):
