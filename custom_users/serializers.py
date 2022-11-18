import bcrypt
from rest_framework import serializers

from custom_users.models import CustomUser
from custom_users.validators import validate_password
from djangoProject.settings import SALTING


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password',)


class CustomUserInSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CustomUser
        validators = [validate_password]

    def create(self, validated_data):
        validated_data["password"] = bcrypt.hashpw(validated_data["password"].encode(), SALTING.encode())
        user = CustomUser(**validated_data)
        try:
            user.save()
        except Exception:
            a = 5
        return user

