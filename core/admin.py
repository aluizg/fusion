from django.contrib import admin
from .models import Servico, Cargo, Equipe, Recurso

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'icone', 'ativo', 'criacao', 'modificacao')
    list_filter = ('ativo',)
    search_fields = ('nome', 'descricao')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'criacao', 'modificacao')
    list_filter = ('ativo',)
    search_fields = ('nome',)

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'criacao', 'modificacao')
    list_filter = ('ativo', 'cargo')
    search_fields = ('nome', 'cargo')

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'icone', 'ativo', 'criacao', 'modificacao')
    list_filter = ('ativo',)
    search_fields = ('titulo', 'descricao')