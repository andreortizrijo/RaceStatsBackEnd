from rest_framework import serializers
from .models import *
from users.serializers import UserSerializer

class SessionSerializer(serializers.ModelSerializer):
    record = UserSerializer(read_only=True, many=False)

    class Meta:
        model = SessionInfo
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackInfo
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInfo
        fields = '__all__'

class CarTyreWearSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTyreWear
        fields = '__all__'

class CarCamberRADSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCamberRAD
        fields = '__all__'

class CarWheelSlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarWheelSlip
        fields = '__all__'

class CarTyreInnerTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTyreInnerTemperature
        fields = '__all__'

class CarTyreMiddleTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTyreMiddleTemperature
        fields = '__all__'

class CarTyreOuterTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTyreOuterTemperature
        fields = '__all__'

class CarTyreCoreTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTyreCoreTemperature
        fields = '__all__'

class CarTyreDirtyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTyreDirtyLevel
        fields = '__all__'

class CarWheelLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarWheelLoad
        fields = '__all__'

class CarBrakeTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrakeTemperature
        fields = '__all__'

class CarDamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDamage
        fields = '__all__'

class CarAccGSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAccG
        fields = '__all__'

class CarWheelPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarWheelPressure
        fields = '__all__'

class CarTyreRadiusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTyreRadius
        fields = '__all__'

class CarSuspensionTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSuspensionTravel
        fields = '__all__'

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeInfo
        fields = '__all__'