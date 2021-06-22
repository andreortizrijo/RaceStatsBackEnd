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
	fuel = models.CharField(max_length=255)
	maxfuel = models.CharField(max_length=255)
	aidfuelrate = models.CharField(max_length=255)
	aidtyrerate = models.CharField(max_length=255)
	aidstability = models.CharField(max_length=255)
	aidautoclutch = models.CharField(max_length=255)
	aidautoblip = models.CharField(max_length=255)
	hasdrs = models.CharField(max_length=255)
	hasers = models.CharField(max_length=255)
	haskers = models.CharField(max_length=255)
	turboboost = models.CharField(max_length=255)
	finalff = models.CharField(max_length=255)
	aicontroll = models.CharField(max_length=255)
	tyrecompound = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarTyreWear(models.Model):
	tyrefl = models.CharField(max_length=255)
	tyrefr = models.CharField(max_length=255)
	tyrerl = models.CharField(max_length=255)
	tyrerr = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarCamberRAD(models.Model):
	tyrefl = models.CharField(max_length=255)
	tyrefr = models.CharField(max_length=255)
	tyrerl = models.CharField(max_length=255)
	tyrerr = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarWheelSlip(models.Model):
	tyrefl = models.CharField(max_length=255)
	tyrefr = models.CharField(max_length=255)
	tyrerl = models.CharField(max_length=255)
	tyrerr = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarTyreInnerTemperature(models.Model):
	tyrefl = models.CharField(max_length=255)
	tyrefr = models.CharField(max_length=255)
	tyrerl = models.CharField(max_length=255)
	tyrerr = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarTyreMiddleTemperature(models.Model):
	tyrefl = models.CharField(max_length=255)
	tyrefr = models.CharField(max_length=255)
	tyrerl = models.CharField(max_length=255)
	tyrerr = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarTyreOuterTemperature(models.Model):
	tyrefl = models.CharField(max_length=255)
	tyrefr = models.CharField(max_length=255)
	tyrerl = models.CharField(max_length=255)
	tyrerr = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarTyreCoreTemperature(models.Model):
	tyrefl = models.CharField(max_length=255)
	tyrefr = models.CharField(max_length=255)
	tyrerl = models.CharField(max_length=255)
	tyrerr = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)
class CarTyreDirtyLevel(models.Model):
	tyrefl = models.CharField(max_length=255)
	tyrefr = models.CharField(max_length=255)
	tyrerl = models.CharField(max_length=255)
	tyrerr = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarWheelLoad(models.Model):
	tyrefl = models.CharField(max_length=255)
	tyrefr = models.CharField(max_length=255)
	tyrerl = models.CharField(max_length=255)
	tyrerr = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarBrakeTemperature(models.Model):
	tyrefl = models.CharField(max_length=255)
	tyrefr = models.CharField(max_length=255)
	tyrerl = models.CharField(max_length=255)
	tyrerr = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarDamage(models.Model):
	section1 = models.CharField(max_length=255)
	section2 = models.CharField(max_length=255)
	section3 = models.CharField(max_length=255)
	section4 = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarSuspensionTravel(models.Model):
	tyrefl = models.CharField(max_length=255)
	tyrefr = models.CharField(max_length=255)
	tyrerl = models.CharField(max_length=255)
	tyrerr = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarAccG(models.Model):
	x = models.CharField(max_length=255)
	y = models.CharField(max_length=255)
	z = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarWheelPressure(models.Model):
	tyrefl = models.CharField(max_length=255)
	tyrefr = models.CharField(max_length=255)
	tyrerl = models.CharField(max_length=255)
	tyrerr = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class CarTyreRadius(models.Model):
	tyrefl = models.CharField(max_length=255)
	tyrefr = models.CharField(max_length=255)
	tyrerl = models.CharField(max_length=255)
	tyrerr = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)

class TimeInfo(models.Model):
	currenttime = models.CharField(max_length=255)
	besttime = models.CharField(max_length=255)
	sessionid = models.ForeignKey(SessionInfo, on_delete=models.CASCADE, default=None)