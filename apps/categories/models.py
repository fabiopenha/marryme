from django.db import models

class Category(models.Model):
    categoria = models.CharField(max_length=100, verbose_name='Categoria')

    def __str__(self):
        return self.categoria