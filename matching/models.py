from matchingpro.models import MatchingPro
from django.db import models
from django.utils import timezone
class Matching(models.Model):
    user = models.ForeignKey(MatchingPro,on_delete=models.CASCADE)
    like = models.CharField(max_length=100,blank =True)
    lked = models.CharField(max_length =100,blank =True)
    matching = models.CharField(max_length= 100,blank =True)
    created_at = models.DateField(default = timezone.now)
