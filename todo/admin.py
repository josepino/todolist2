from django.contrib import admin

from models import *


class FaseAdmin(admin.TabularInline):
    """
    Definicion de la clase FaseAdmin
    """
    list_display = ('Proyecto', 'Nombre', "Descripcion", "FechaCreacion",)
    list_filter = ( 'FechaCreacion', 'FechaInicio', 'Estado',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)
    model = Fase
    extra = 0


class ProyectoAdmin(admin.ModelAdmin):
    """
    Definicion de la clase Proyecto
    """
    list_display = ('Nombre', "Descripcion", "FechaCreacion",)
    list_filter = ( 'FechaCreacion', 'FechaInicio', 'Estado',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)
    inlines = [FaseAdmin]


admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Fase)

