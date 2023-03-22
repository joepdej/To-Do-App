from django import forms
from .models import Taak

class TaakForm(forms.ModelForm):
    class Meta:
        model = Taak
        fields = ['titel', 'beschrijving', 'compleet', 'datumKlaar']
        widgets = {
            'datumKlaar': forms.DateInput(format=('%d-%m-%Y'), attrs={'type': 'date'})
        }