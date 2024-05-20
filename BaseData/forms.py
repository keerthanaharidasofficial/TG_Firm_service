from django import forms
from .models import *

class baseDataForm(forms.ModelForm):
    class Meta:
        model = BaseData
        fields = '__all__'