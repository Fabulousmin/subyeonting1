from rest_framework import generics

from . import models
from . import serializers

class ProfileListView(generics.ListCreateAPIView):
    queryset = models.Profiles.objects.all()
    serializer_class = serializers.ProfilesSerializer
