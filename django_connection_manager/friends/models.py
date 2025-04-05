from django.db import models
from django.contrib.auth.models import User

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friends")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)
    birthday = models.DateField(null=True, blank=True)
    platform = models.CharField(max_length=100, help_text="SNS種別やプラットフォーム名")
    contact_info = models.CharField(max_length=200, blank=True)
    last_met_date = models.DateField(null=True, blank=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)