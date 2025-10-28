from django import forms
from .models import Film

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Film
        field = '__all__'
