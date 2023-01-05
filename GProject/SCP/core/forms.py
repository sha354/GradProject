from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

# Sign up form
class UserCreationForms(UserCreationForm):
    # 2\ determine charcterstics of each field in the form
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    password1 = forms.CharField(label='Password:',widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Confirmation:', widget=forms.PasswordInput())

    class Meta:
        model= User
        fields = ('first_name','last_name','username', 'password1', 'password2')  # 1\Select models field

# Login form
class LoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields = ('username', 'password')


# Update User Data
class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


# Update User Data
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('name', 'about', 'img')

