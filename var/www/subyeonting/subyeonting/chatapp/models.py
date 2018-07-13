from userinfo.models import UserInfo
from django.db import models
class Message(models.Model):
     sender = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='sender')
     receiver = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='receiver')
     message = models.CharField(max_length=1200)
     photo = models.ImageField(blank =True)
     timestamp = models.DateTimeField(auto_now_add=True)
     is_read = models.BooleanField(default=False)
     def __str__(self):
           return self.message
     class Meta:
           ordering = ('timestamp',)
