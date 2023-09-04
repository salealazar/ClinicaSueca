from django import forms
from django.contrib.auth.forms import UserCreationForm
from clinicaSuecaApp.models import Persona, HoraMedica

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model=Persona
        fields = ['username','email','password1','password2']

class BookForm(forms.ModelForm):
    inicio = forms.DateTimeField()
    termino = forms.DateTimeField()
    sucursal = forms.Select(choices=[(1, 'Barcelona'), (2, 'Madrid')])
    class Meta:
        model=HoraMedica
        fields=['doctor', 'inicio', 'termino', 'sucursal']