from rest_framework import serializers
from . import models

class MatchingProSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MatchingPro
        fields = ('nickname','derscription','photos','number')
