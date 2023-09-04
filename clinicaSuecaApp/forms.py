from django import forms
from django.contrib.auth.forms import UserCreationForm
from clinicaSuecaApp.models import Persona

class LoginForm(forms.Form):
    rut = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model=Persona
        fields = ['rut','email','password1','password2']