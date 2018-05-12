from django.db import models

from django.db import models
from django.utils import timezone

class DeviceToken(models.Model):
    token = models.CharField(max_length=256)
    created_date = models.DateTimeField(default=timezone.now)

