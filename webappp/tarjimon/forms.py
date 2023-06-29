from django import forms
from .models import Word


class AddWordForm(forms.ModelForm):
    class Meta:
        model=Word
        fields='__all__'


