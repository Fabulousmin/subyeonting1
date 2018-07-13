# users/serializers.py
from rest_framework import serializers
from . import models

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = '__all__'
