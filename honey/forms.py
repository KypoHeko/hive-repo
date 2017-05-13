from django import forms
from .models import Persona

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PersonaForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ('surname', 'name', 'age', 'occupation', 'worldview', 'quote',)

"""
class SignUpForm(UserCreationForm):
    user = forms.EmailField(max_length=64)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)"""