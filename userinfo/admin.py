from django.contrib import admin
from .models import UserInfo

# Register your models here.
@admin.register(UserInfo)
class UserinfoAdmin(admin.ModelAdmin):
    list_display = ['age','city','sex','user']
