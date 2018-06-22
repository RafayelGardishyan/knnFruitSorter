from django.contrib import admin
from .models import Fruit
# Register your models here.

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    pass