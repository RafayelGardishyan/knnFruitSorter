from django.db import models

# Create your models here.
class Fruit(models.Model):
    colors = (
        (1, 'Red'),
        (2, 'Orange'),
        (3, 'Yellow'),
        (4, 'Green'),
        (5, 'Blue'),
        (6, 'Purple'),
    )
    shapes = (
        (1, 'Long & thin'),
        (2, 'Long & thick'),
        (3, 'Round'),
        (4, 'Round & flat'),
        (5, 'Cone'),
    )

    textures = (
        (1, 'Smooth'),
        (2, 'Soft'),
        (3, 'Hairy'),
        (4, 'Hard'),
        (5, 'Velvet'),
        (6, 'Juicy')
    )

    name = models.CharField(max_length=100)
    size = models.IntegerField()
    texture = models.IntegerField(choices=textures)
    shape = models.IntegerField(choices=shapes)
    color = models.IntegerField(choices=colors)
