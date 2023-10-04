from django import forms
from .models import Customeuser
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreation(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model=Customeuser
        fields=[ 'username','email', 'password1', 'password2', 'username','mobile','userimg']
        
