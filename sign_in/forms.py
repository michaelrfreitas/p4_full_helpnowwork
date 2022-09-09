from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser


class MyCustomSignupForm(SignupForm):

    PROFILES = (
        ('USER', 'USER'),
        ('CONTRIBUTOR', 'CONTRIBUTOR')
    )

    first_name = forms.CharField(max_length=30, label='First Name',
                    widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name',
                    widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    mobile = forms.CharField(max_length=20,
                    widget=forms.TextInput(attrs={'placeholder': '+353 XX XXX XXXX'}))
    profile = forms.ChoiceField(choices=PROFILES)


    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.mobile = self.cleaned_data['mobile']
        user.profile = self.cleaned_data['profile']
        user.save()
        return user
