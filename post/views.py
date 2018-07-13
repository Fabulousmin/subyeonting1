from rest_framework import generics
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

class PostListView(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    def perform_create(self, serializer):
        serializer.save(
        author = self.request.user)



class PostDetailListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    def perform_create(self, serializer):
        serializer.save(
        author = self.request.user)
    permission_classes = [
            IsAuthenticatedOrReadOnly,
    ]
