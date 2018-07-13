from django.db import models
from django.utils import timezone
from users.models import CustomUser

class UserInfo(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    created_at = models.DateField(default = timezone.now)
    def __str__(self):
        return self.nickname
