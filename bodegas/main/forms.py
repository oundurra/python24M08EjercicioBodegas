from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TipoBodega

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obligatorio')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class TipoBodegaForm(forms.Form):
    tipo_bodega = forms.ModelChoiceField(queryset=TipoBodega.objects.all(), required=True)