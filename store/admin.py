from django.contrib import admin
from .models import Category,Shop,Review,Item



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','icon']

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display =['name','photo']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author','photo','rating','message']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','desc','amount','photo']
