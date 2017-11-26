from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class registerForm(UserCreationForm):
    """
    Extends the UCF to add extra fields
    """
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')
