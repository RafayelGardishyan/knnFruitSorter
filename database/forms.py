from django import forms
from .models import Fruit
from .constants import SHAPES, TEXTURES, COLORS


class FruitForm(forms.Form):
    size = forms.IntegerField(label="Size (cm)", max_value=100)
    color = forms.ChoiceField(choices=COLORS, widget=forms.Select)
    texture = forms.ChoiceField(choices=TEXTURES, widget=forms.Select)
    shape = forms.ChoiceField(choices=SHAPES, widget=forms.Select)
