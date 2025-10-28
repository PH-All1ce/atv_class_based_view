from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao', 'lancamento', 'genero', 'diretor')
    fields = ('nome', 'duracao', 'lancamento', 'genero', 'diretor')