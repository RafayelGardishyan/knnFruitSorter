from django import forms
from .models import Fruit
colors = (
        (1, 'Red'),
        (2, 'Orange'),
        (3, 'Yellow'),
        (4, 'Green'),
        (5, 'Blue'),
        (6, 'Purple'),
        (7, 'Brown')
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


class FruitForm(forms.Form):
    size = forms.IntegerField(label="Size (cm)")
    color = forms.ChoiceField(choices=colors, widget=forms.Select)
    texture = forms.ChoiceField(choices=textures, widget=forms.Select)
    shape = forms.ChoiceField(choices=shapes, widget=forms.Select)
