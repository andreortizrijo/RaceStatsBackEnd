from django.db import models
from django.contrib.auth.models import AbstractUser
import teams.models as team

class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    team = models.ForeignKey(team.Team, on_delete=models.CASCADE, default=None, null=True)

    REQUIRED_FIELDS = []

class WhiteList(models.Model):
    token = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=False)
    userid = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

class BlackList(models.Model):
    token = models.CharField(max_length=255)