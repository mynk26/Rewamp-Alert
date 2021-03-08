from django.contrib.auth.forms import UserCreationForm
from .models import useraccount
from django.forms import Form
from django import forms
class SignupForm(UserCreationForm):
    class Meta:
        model = useraccount
        fields = ('first_name','last_name','email','username', 'password1', 'password2')

class LoginForm(Form):
    username =forms.CharField(max_length=150)
    password=forms.CharField(max_length=32,widget=forms.PasswordInput)