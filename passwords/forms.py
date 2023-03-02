from django.forms import ModelForm, TextInput
from django import forms
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'bg-gray-50 border my-2 border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-gray-50 border my-2 border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-gray-50 border my-2 border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class PasswordForm(ModelForm):
    class Meta:
        model = Password_data
        fields = "__all__"

        widgets = {
            'name': TextInput(attrs={'class': 'border border-gray-400 p-2 rounded-lg'}),
            'password': forms.PasswordInput(attrs={"class": "border border-gray-400 p-2 rounded-lg"}),
            'user': forms.HiddenInput(),
        }



