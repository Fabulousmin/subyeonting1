from matchingpro.models import MatchingPro
from rest_framework import serializers
from .models import Message
from users.models import CustomUser
from matchingpro.serializers import MatchingProSerializer
#
# User Serializer
class UserSerializer(MatchingProSerializer):
    class Meta:
        model = MatchingPro
        fields = ['nickname']
#
# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    sender = serializers.SlugRelatedField(many=False, slug_field='nickname', queryset=MatchingPro.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='nickname', queryset=MatchingPro.objects.all())
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message','is_read','photo','timestamp']
