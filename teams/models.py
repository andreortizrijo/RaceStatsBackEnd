from django.db import models
from django.conf import settings

class Team(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

class Manager(models.Model):
	userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
	teamid = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)