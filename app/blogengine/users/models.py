from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(verbose_name="Name of user",blank=True,max_length=255)

    def __str__(self):
        return self.username
