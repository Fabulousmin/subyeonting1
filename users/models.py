from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length= 255)
    created_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.email
