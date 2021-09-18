from rest_framework import serializers
from .models import User, WhiteList, BlackList

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'team']
        extra_kwargs = {
            'password':{'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance

class WhiteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhiteList
        fields = '__all__'

class BlackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackList
        fields = '__all__'