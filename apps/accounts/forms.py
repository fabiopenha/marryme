from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, label="Nome")
    last_name = forms.CharField(max_length=100, label="Sobrenome")
    empresa = forms.CharField(max_length=100, label="Empresa")
    telefone = forms.CharField(max_length=100, label="Telefone")
    CATEGORIAS_CHOICES = (
        ('Salão de Festa', 'Salão de Festa'),
        ('Espaço para Cerimônia', 'Espaço para Cerimônia'),
        ('Equipe de Beleza', 'Equipe de Beleza'),
        ('Equipe de Fotografia e Filmasgens', 'Equipe de Fotografia e Filmagens'),
        ('Buffet', 'Buffet'),
        ('Lua de mel', 'Lua de mel'),
    )
    categoria = forms.ChoiceField(choices=CATEGORIAS_CHOICES)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','empresa','telefone','categoria', 'email', 'password1', 'password2')


class PasswordsChangeView:
    pass