from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = ['name','photo']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ['author','photo','rating','message']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ['name','desc','amount','photo']
