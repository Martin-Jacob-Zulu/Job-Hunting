from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UserAccount


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text="Required. Add a valid email")

    class Meta:
        model = UserAccount
        fields = ("name", "email", "username", "password1", "password2")