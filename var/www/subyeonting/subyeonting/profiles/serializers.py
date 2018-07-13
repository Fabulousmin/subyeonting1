from rest_framework import serializers
from . import models

class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profiles
        fields = ('nickname','age','photo','derscription')
        
