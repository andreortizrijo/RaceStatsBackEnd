from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    REQUIRED_FIELDS = []

class WhiteList(models.Model):
    token = models.CharField(max_length=255, unique=True)

class BlackList(models.Model):
    token = models.CharField(max_length=255)