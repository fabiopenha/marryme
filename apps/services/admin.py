from django.contrib import admin
from .models import Services
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_titulo', 'usuario', 'data_public', 'service_imagem','categoria','ativo')
    list_display_links = ('service_titulo',)


admin.site.register(Services, ServicesAdmin)

