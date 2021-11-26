from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    empresa = models.CharField(max_length=100, verbose_name='Empresa')
    nome = models.CharField(max_length=100, verbose_name='Nome')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    telefone = models.CharField(max_length=100, verbose_name='Telefone')
    CATEGORIAS_CHOICES = (
        ('Salão de Festa', 'Salão de Festa'),
        ('Espaço para Cerimônia', 'Espaço para Cerimônia'),
        ('Equipe de Beleza', 'Equipe de Beleza'),
        ('Equipe de Fotografia e Filmasgens', 'Equipe de Fotografia e Filmagens'),
        ('Buffet', 'Buffet'),
        ('Lua de mel', 'Lua de mel'),
    )
    categoria = models.CharField(max_length=100, choices=CATEGORIAS_CHOICES)

    def __str__(self):
        return self.usuario.username

