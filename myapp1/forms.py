from django import forms
from .models import game

class gameform(forms.Form):
   name = forms.CharField(label='name', max_length=14, required=True)
   description = forms.DateField(label="description",required=True)