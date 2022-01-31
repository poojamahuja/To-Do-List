from django.db import models
from django.contrib.auth.models import AbstractUser


class Task(AbstractUser):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
