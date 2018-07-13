from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length =100)
    icon = models.ImageField(blank =True)

    def __str__(self):
        return self.name

class Shop(models.Model):
    Categoty = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length =100)
    photo =models.ImageField(blank =True,upload_to ='shop/%Y/%m/%d')

    def __str__(self):
        return self.name

class Review(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    photo =models.ImageField(blank =True,upload_to ='review/%Y/%m/%d')
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    message = models.TextField()

class Item(models.Model):
    shop = models.ForeignKey(Shop,on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField(blank =True)
    amount = models.PositiveIntegerField()
    photo = models.ImageField(blank =True,upload_to ='item/%Y/%m/%d')

    def __str__(self):
        return self.name


class Order(models.Model):
    pass
