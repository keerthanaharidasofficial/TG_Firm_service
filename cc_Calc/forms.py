from django import forms
from .models import *
from django.contrib.auth.models import User
class dataEntryForm(forms.ModelForm):
    class Meta:
        model = TariffEntry
        fields = ['customer','load_plan','destination','value','wt','commodity','VAT_claim']
        labels = {
            'customer':'Customer Name',
            'wt':'Weight',
            'VAT_claim':'VAT Claim Required'
        }
class staff_login(forms.Form):
    username = forms.CharField(max_length=40,initial='admin')
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)

    labels = {
        'username' : 'Username',
        'password' : 'Password'
    }