from rest_framework import generics

from . import models
from . import serializers

class MatchingListView(generics.ListCreateAPIView):
    queryset = models.Matching.objects.all()
    serializer_class = serializers.MatchingSerializer
