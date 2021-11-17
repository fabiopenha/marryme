from django.db import models
from apps.accounts.models import Usuario
from django.utils import timezone


class Services(models.Model):
    service_titulo = models.CharField(max_length=255,verbose_name='Título')
    service_descricao = models.TextField(verbose_name='Descrição')
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, verbose_name="Usuário")
    data_public = models.DateTimeField(default=timezone.now, verbose_name='Data da Publicação')
    service_imagem = models.ImageField(upload_to='imagens/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    ativo = models.BooleanField(default=False)