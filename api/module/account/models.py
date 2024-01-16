import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=True, blank=True, default=None)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True, default=None)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True, default=None)
    weight = models.FloatField(blank=True, null=True, default=None)

    def __str__(self):
        return self.username

