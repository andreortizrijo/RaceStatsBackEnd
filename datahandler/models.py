from django.db import models
from django.conf import settings

class SessionInfo(models.Model):
	rack = models.CharField(max_length=255)
	trackconfiguration = models.CharField(max_length=255)
	userid = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='record')

class TrackInfo(models.Model):
	sectorcount = models.CharField(max_length=255)
	airdensity = models.CharField(max_length=255)
	airtemperature = models.CharField(max_length=255)
	roadtemperature = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarInfo(models.Model):
	speedkmh = models.CharField(max_length=255)
	rpm = models.CharField(max_length=255)
	gear = models.CharField(max_length=255)
	gaspedal = models.CharField(max_length=255)
	brakepedal = models.CharField(max_length=255)
	clutchpedal = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)