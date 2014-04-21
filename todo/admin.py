from django.contrib import admin

from models import *


class FaseAdmin(admin.TabularInline):
    """
    Definicion de la clase FaseAdmin
    """
    list_display = ('Nombre',)
    list_filter = ('Nombre',)
    search_fields = ['Nombre']
    model = Fase
    extra = 0


class ProyectoAdmin(admin.ModelAdmin):
    """
    Definicion de la clase de Administracion de Proyecto
    """
    list_display = ('Nombre', "Descripcion", "FechaCreacion",)
    list_filter = ('Nombre', "FechaCreacion",)
    search_fields = ['Nombre']
    ordering = ('Nombre',)
    #inlines = [FaseAdmin]



admin.site.register(Proyecto, ProyectoAdmin)
#admin.site.register(Fase)

