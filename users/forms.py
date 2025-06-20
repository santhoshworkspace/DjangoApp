from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationFrom(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

