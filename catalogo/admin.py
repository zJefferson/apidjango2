#Criar admin.py
from django.contrib import admin

# Register your models here.

from .models import Filme, Avaliacao

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvalicaoAdmin(admin.ModelAdmin):
    list_display = ('filme', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')
