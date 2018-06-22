from django.db import models
from .constants import SHAPES, TEXTURES, COLORS

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    texture = models.IntegerField(choices=TEXTURES)
    shape = models.IntegerField(choices=SHAPES)
    color = models.IntegerField(choices=COLORS)
