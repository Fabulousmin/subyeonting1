from django.db import models

from userinfo.models import UserInfo


class Profiles(UserInfo):
    derscription = models.TextField()
