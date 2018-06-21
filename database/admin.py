from django.contrib import admin
from .models import Fruit
# Register your models here.

class FruitAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fruit, FruitAdmin)