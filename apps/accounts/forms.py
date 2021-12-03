from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, label="Usuário", widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Usuário'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','type':'email','placeholder':'E-mail'}))
    first_name = forms.CharField(max_length=100, label="Nome", widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Nome'}))
    last_name = forms.CharField(max_length=100, label="Sobrenome", widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Sobrenome'}))
    empresa = forms.CharField(max_length=100, label="Empresa", widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Empresa'}))
    telefone = forms.CharField(max_length=100, label="Telefone",widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Telefone'}))
    password1 = forms.CharField(max_length=100,label='Senha', widget=forms.PasswordInput(attrs={'class':'form-control','type':'password','placeholder':'Senha'}))
    password2 = forms.CharField(max_length=100,label='Confirmarção de Senha', widget=forms.PasswordInput(attrs={'class':'form-control','type':'password','placeholder':'Confirmação de Senha'}))
    CATEGORIAS_CHOICES = (
        ('Salão de Festa', 'Salão de Festa'),
        ('Espaço para Cerimônia', 'Espaço para Cerimônia'),
        ('Equipe de Beleza', 'Equipe de Beleza'),
        ('Equipe de Fotografia e Filmasgens', 'Equipe de Fotografia e Filmagens'),
        ('Buffet', 'Buffet'),
        ('Lua de mel', 'Lua de mel'),
    )
    categoria = forms.ChoiceField(choices=CATEGORIAS_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'empresa',
                  'telefone',
                  'categoria',
                  'email',
                  'password1',
                  'password2')


class PasswordsChangeView:
    pass