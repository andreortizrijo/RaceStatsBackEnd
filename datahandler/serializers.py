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

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeInfo
        fields = '__all__'