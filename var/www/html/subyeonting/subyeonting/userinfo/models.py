from django.db import models
from django.utils import timezone

class UserInfo(models.Model):
    # nickname = models.CharField(max_length=100,unique=True,blank =True)
    # age = models.IntegerField(blank =True)
    # city = models.TextField(blank =True)
    sex = models.CharField(max_length = 100, blank=True)
    # photo = models.ImageField(blank =True)
    created_at = models.DateField(default = timezone.now)
