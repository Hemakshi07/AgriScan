from django import forms
from .validators import validate_password, validate_username_length

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[validate_username_length])
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class': 'form-control'}),validators=[validate_password])

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

   
