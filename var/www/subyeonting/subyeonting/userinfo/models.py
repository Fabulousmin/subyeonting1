from django.db import models
from django.utils import timezone

class UserInfo(models.Model):
    nickname = models.CharField(max_length=100,unique=True)
    age = models.IntegerField()
    city = models.TextField()
    sex = models.CharField(max_length = 100)
    photo = models.ImageField(blank =True)
    created_at = models.DateField(default = timezone.now)
