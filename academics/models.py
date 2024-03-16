from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class IdentificationType(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
