from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import serializers
from . import models

class CategroyListView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CategroyDeatailListView(generics.RetrieveAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ShopListView(generics.ListAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer


class ShopDetailListView(generics.RetrieveAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer


class ItemListView(generics.ListAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

class ItemDetailListView(generics.RetrieveAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer


class ReviewListView(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReviewDetailListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
