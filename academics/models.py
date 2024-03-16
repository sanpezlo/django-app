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


class Country(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Department(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class City(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    id_dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
