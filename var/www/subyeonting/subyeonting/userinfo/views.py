from rest_framework import generics

from . import models
from . import serializers

class UserListView(generics.ListCreateAPIView):
    queryset = models.UserInfo.objects.all()
    serializer_class = serializers.UserInfoSerializer


class UserDetailListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UserInfo.objects.all()
    serializer_class = serializers.UserInfoSerializer
