from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Words

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Enter your email')
    full_name = forms.CharField(required=True, help_text='Enter your full name')
    phone = forms.CharField(required=True, max_length=10, help_text='Enter your phone number')
            
    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'phone', 'password1', 'password2']



