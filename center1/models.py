from django.db import models
from store.models import Category



class Center(models.Model):
    category = models.ForeignKey(Category,models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField()

class Shop(models.Model):
    Category = models.ForeignKey(Center, models.CASCADE)
    name = models.CharField(max_length =100)
    photo = models.ImageField(blank =True)


class Item(models.Model):
    shop = models.ForeignKey(Shop,on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField(blank =True)
    amount = models.PositiveIntegerField()
    photo = models.ImageField()


class Review(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    photo =models.ImageField(blank =True)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    message = models.TextField()
