from rest_framework import serializers
from .models import SessionInfo, TrackInfo, CarInfo

class SessionSerializer(serializers.ModelSerializer):
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