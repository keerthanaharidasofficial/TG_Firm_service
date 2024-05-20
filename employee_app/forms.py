from django import forms
from .models import *

class employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'