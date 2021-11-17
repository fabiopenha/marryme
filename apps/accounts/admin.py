from django.contrib import admin
from apps.accounts.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario','empresa', 'telefone', 'categoria')
    list_display_links = ('usuario',)

admin.site.register(Usuario, UsuarioAdmin)
