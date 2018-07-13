from django.db import models
from users.models import CustomUser

class MatchingPro(models.Model):
    user_profile = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100,unique=True, default=" ")
    derscription = models.TextField()
    number  = models.IntegerField()
    photos =models.ImageField(blank = True, upload_to ='Matchingpro/%Y/%m/%d')
    def __str__(self):
          return self.nickname
