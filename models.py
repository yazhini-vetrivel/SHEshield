from django.db import models
from django.contrib.auth.models import User

class EmergencyContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15) # Format: +919876543210

class UnsafeAreaReport(models.Model):
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    risk_level = models.IntegerField(default=1) # 1-5 scale
    timestamp = models.DateTimeField(auto_now_add=True)
