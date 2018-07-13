from userinfo.models import UserInfo
from rest_framework import serializers
from .models import Message
from userinfo.serializers import UserInfoSerializer
#
# User Serializer
class UserSerializer(UserInfoSerializer):
    class Meta:
        model = UserInfo
        fields = ['nickname']
#
# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    sender = serializers.SlugRelatedField(many=False, slug_field='nickname', queryset=UserInfo.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='nickname', queryset=UserInfo.objects.all())
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message','is_read','photo','timestamp']
