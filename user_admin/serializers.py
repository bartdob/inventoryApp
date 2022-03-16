from abc import ABC
from rest_framework import serializers
from .models import CustomUser, Roles


class CreateUserSerializer(serializers.Serializer, ABC):
    email = serializers.EmailField()
    fullname = serializers.CharField()
    role = serializers.ChoiceField(Roles)


class LoginSerializer(serializers.Serializer, ABC):
    email = serializers.EmailField()
    password = serializers.CharField(required=False)
    is_new_user = serializers.BooleanField(default=False, required=False)
