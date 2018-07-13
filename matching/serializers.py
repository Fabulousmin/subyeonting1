# users/serializers.py
from rest_framework import serializers
from . import models

class MatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Matching
        fields = '__all__'
