from django.contrib import admin

from models import *


class ItemAdmin(admin.ModelAdmin):
    """
    Definicion de la clase ItemAdmin
    """
    list_display = (
    'Nombre', 'TipoItem', 'Descripcion', 'Complejidad', 'Estado', 'Version', 'Costo', 'FechaModificacion',)
    list_filter = ( 'TipoItem', 'Complejidad', 'Estado', 'Costo', 'FechaModificacion',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)


class ItemAdmin2(admin.TabularInline):
    """
    Definicion de la clase ItemAdmin2 que se utiliza para la clase FaseAdmin
    """
    ordering = ('Nombre',)
    model = Item
    extra = 0


class TipoItemAdmin(admin.ModelAdmin):
    """
    Definicion de la clase TipoItemAdmin
    """
    list_display = ('Nombre', 'Fase', 'Descripcion',)
    list_filter = ( 'Fase',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)
    inlines = [ItemAdmin2]


class TipoItemAdmin2(admin.TabularInline):
    """
    Definicion de la clase TipoItemAdmin2 que se utiliza para la clase FaseAdmin
    """
    ordering = ('Nombre',)
    model = TipoItem
    extra = 0


class FaseAdmin(admin.ModelAdmin):
    """
    Definicion de la clase FaseAdmin
    """
    list_display = ('Nombre', 'fkproyecto', 'Descripcion', 'FechaCreacion',)
    list_filter = ( 'fkproyecto', 'FechaCreacion', 'FechaInicio', 'Estado',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)
    inlines = [TipoItemAdmin2]


class FaseAdmin2(admin.TabularInline):
    """
    Definicion de la clase FaseAdmin2 que se utiliza para la clase ProyectoAdmin
    """
    ordering = ('Nombre',)
    model = Fase
    extra = 0


class ProyectoAdmin(admin.ModelAdmin):
    """
    Definicion de la clase ProyectoAdmin
    """
    list_display = ('Nombre', 'Descripcion', 'FechaCreacion',)
    list_filter = ( 'FechaCreacion', 'FechaInicio', 'Estado',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)
    inlines = [FaseAdmin2]


admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Fase, FaseAdmin)
admin.site.register(TipoItem, TipoItemAdmin)
admin.site.register(Item, ItemAdmin)

