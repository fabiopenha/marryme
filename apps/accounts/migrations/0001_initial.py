# Generated by Django 3.2.9 on 2021-11-26 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=100, verbose_name='Empresa')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=100, verbose_name='Telefone')),
                ('categoria', models.CharField(choices=[('Salão de Festa', 'Salão de Festa'), ('Espaço para Cerimônia', 'Espaço para Cerimônia'), ('Equipe de Beleza', 'Equipe de Beleza'), ('Equipe de Fotografia e Filmasgens', 'Equipe de Fotografia e Filmagens'), ('Buffet', 'Buffet'), ('Lua de mel', 'Lua de mel')], max_length=100)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
