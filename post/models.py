from django.db import models
from django.utils import timezone
from users.models import CustomUser

class Post(models.Model):
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post_photo = models.ImageField(blank =True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
