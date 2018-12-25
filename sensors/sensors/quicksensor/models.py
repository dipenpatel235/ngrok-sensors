from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
import uuid

class Sensors(models.Model):

    ip = models.GenericIPAddressField(max_length=100)
    sensorid = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    deployed = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)