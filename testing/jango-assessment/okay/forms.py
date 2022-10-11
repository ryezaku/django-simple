from django.forms import ModelForm
from django import forms
from .models import Score
class Keyin(ModelForm):
    name = forms.TextInput()
    score = forms.NumberInput()
    class Meta:
        model = Score
        fields = ['name', 'score']

