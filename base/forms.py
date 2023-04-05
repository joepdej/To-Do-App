from django import forms
from django.contrib.auth.models import User
from .models import Taak


class TaakForm(forms.ModelForm):
    class Meta:
        model = Taak
        fields = ['titel', 'beschrijving', 'compleet', 'datumKlaar']
        widgets = {
            'datumKlaar': forms.DateInput(format=('%d-%m-%Y'), attrs={'type': 'date'})
        }

class InviteUserForm(forms.Form):
    username = forms.CharField(label='Gebruikersnaam', max_length=100)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Gebruiker niet gevonden')
        return username
