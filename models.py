from django.db import models
from django.contrib.auth.models import User

class EmergencyContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class UnsafeArea(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    risk_level = models.IntegerField(default=3)
    description = models.TextField(blank=True)
