from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text="Required. Add a valid email")

    class Meta:
        model = Account
        fields = ("name", "email", "username", "password1", "password2")