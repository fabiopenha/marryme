from django.contrib import admin
from apps.categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria')
    list_display_links = ('categoria',)


admin.site.register(Category, CategoryAdmin)

