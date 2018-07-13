from django.contrib import admin
from .models import MatchingPro

# Register your models here.
@admin.register(MatchingPro)
class MatchingProAdmin(admin.ModelAdmin):
    list_display = ['derscription','photos']
