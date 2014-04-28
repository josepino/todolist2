from django.contrib import admin

from models import *


class TipoItemAdmin(admin.ModelAdmin):
    """
    Definicion de la clase TipoItemAdmin
    """
    list_display = ("Nombre", "Descripcion", "Fase",)
    list_filter = ( 'Fase',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)


class FaseAdmin(admin.TabularInline):
    """
    Definicion de la clase FaseAdmin
    """
    list_display = ("Nombre", "Descripcion", "FechaCreacion",)
    list_filter = ( 'FechaCreacion', 'FechaInicio', 'Estado',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)
    model = Fase
    extra = 0


class ProyectoAdmin(admin.ModelAdmin):
    """
    Definicion de la clase ProyectoAdmin
    """
    list_display = ("Nombre", "Descripcion", "FechaCreacion",)
    list_filter = ( 'FechaCreacion', 'FechaInicio', 'Estado',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)
    inlines = [FaseAdmin]


admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Fase)
admin.site.register(TipoItem, TipoItemAdmin)

