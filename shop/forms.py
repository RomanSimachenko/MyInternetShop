from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


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
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name',
                  'last_name', 'email', 'phone', 'birth_date', 'password1', 'password2')
