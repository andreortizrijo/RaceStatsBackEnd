from django.db import models
from django.conf import settings

class SessionInfo(models.Model):
	track = models.CharField(max_length=255)
	trackconfiguration = models.CharField(max_length=255, null=True)
	record = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='record')

class TrackInfo(models.Model):
	splinelength = models.CharField(max_length=255)
	sectorcount = models.CharField(max_length=255)
	airdensity = models.CharField(max_length=255)
	airtemperature = models.CharField(max_length=255)
	roadtemperature = models.CharField(max_length=255)
	windspeed = models.CharField(max_length=255)
	winddirection = models.CharField(max_length=255)
	surfacegrip = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarInfo(models.Model):
	model = models.CharField(max_length=255)
	sponser = models.CharField(max_length=255)
	speedkmh = models.CharField(max_length=255)
	rpm = models.CharField(max_length=255)
	gear = models.CharField(max_length=255)
	gaspedal = models.CharField(max_length=255)
	brakepedal = models.CharField(max_length=255)
	clutchpedal = models.CharField(max_length=255)
	steerangle = models.CharField(max_length=255)
	tyrecompound = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class TimeInfo(models.Model):
	currenttime = models.CharField(max_length=255)
	besttime = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)