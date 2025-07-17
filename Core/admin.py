from django.contrib import admin
from .models import Pagina

@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'autor', 'creado_en')
    search_fields = ('titulo', 'contenido')