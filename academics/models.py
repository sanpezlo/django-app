from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
