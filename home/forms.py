from django import forms
from .models import SupportModel


class SupportForm(forms.ModelForm):
    class Meta:
        model = SupportModel
        fields = ['subject', 'details', 'email']
