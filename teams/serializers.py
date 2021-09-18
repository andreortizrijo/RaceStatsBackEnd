from rest_framework import serializers
from users.serializers import UserSerializer
from .models import *

class TeamSerializer(serializers.ModelSerializer):
	owner = UserSerializer(read_only=True, many=False)

	class Meta:
		model = Team
		fields = '__all__'

class MnagerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Manager
		fields = '__all__'