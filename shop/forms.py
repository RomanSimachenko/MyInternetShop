from distutils.command.build_scripts import first_line_re
from re import T
from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django.contrib.auth import password_validation


class CustomUserLoginForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'password',)


class CustomUserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150, required=True)
    last_name = forms.CharField(
        max_length=150, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(
        max_length=16, required=True)
    birth_date = forms.DateField(
        required=True, help_text="Format: year-month-day")

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name',
                  'last_name', 'email', 'phone', 'birth_date', 'password1', 'password2')
