from django.forms import ModelForm
from django import forms
from .models import *

class PasswordForm(ModelForm):
    class Meta:
        model = Password
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
        }



