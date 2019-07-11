from rest_framework import serializers
from core.models import TestModel
from django.contrib.auth.models import User


class TestModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TestModel
        fields = ('id', 'name', 'email', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'users')
