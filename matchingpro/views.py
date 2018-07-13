from rest_framework import generics
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated

class MatchingProListView(generics.ListCreateAPIView):
    queryset = models.MatchingPro.objects.all()
    serializer_class = serializers.MatchingProSerializer
    def perform_create(self, serializer):
        serializer.save(
        user_profile = self.request.user)
    permission_classes = [
            IsAuthenticated
    ]



class MatchingProDetailListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MatchingPro.objects.all()
    serializer_class = serializers.MatchingProSerializer
    def perform_create(self, serializer):
        serializer.save(
        user_profile = self.request.user)
    permission_classes = [
            IsAuthenticated
    ]
