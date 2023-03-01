from django.forms import ModelForm, TextInput
from django import forms
from .models import *

class PasswordForm(ModelForm):
    class Meta:
        model = Password_data
        fields = "__all__"

        widgets = {
            'name': TextInput(attrs={'class': 'border border-gray-400 p-2 rounded-lg'}),
            'password': forms.PasswordInput(attrs={"class": "border border-gray-400 p-2 rounded-lg"}),
            'user': forms.HiddenInput(),
        }



