from rest_framework import generics
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class UserListView(generics.ListCreateAPIView):
    queryset = models.UserInfo.objects.all()
    serializer_class = serializers.UserInfoSerializer
    permission_classes = [
            IsAuthenticated,
    ]



class UserDetailListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UserInfo.objects.all()
    serializer_class = serializers.UserInfoSerializer
    permission_classes = [
            IsAuthenticated,
    ]
