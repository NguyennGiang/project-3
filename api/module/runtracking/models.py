import os
import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.

def img_destination(instance, filename):
    ext = filename.split(".")[-1]
    return os.path.join("running", f"{uuid.uuid4()}.{ext}")


class RunningTracking(models.Model):
    img = models.ImageField(upload_to=img_destination, blank=True, null=True)
    timestamp = models.DateTimeField()
    avgSpeed = models.FloatField(blank=True, null=True, default=0.0)
    distance = models.IntegerField(blank=True, null=True, default=0.0)
    time = models.IntegerField(blank=True, null=True, default=0.0)
    caloriesBurned = models.FloatField(blank=True, null=True, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='running_tracking')

    class Meta:
        db_table = "running_tracking"
        ordering = ["-id"]
