from django.contrib import admin

from models import *


class LineaBaseAdmin(admin.ModelAdmin):
    """
    Definicion de la clase LineaBaseAdmin
    """
    list_display = ('Nombre', 'Fase', 'FechaCreacion', 'Estado',)
    list_filter = ( 'Fase', 'FechaCreacion', 'Estado',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)


class RelacionAdmin(admin.ModelAdmin):
    """
    Definicion de la clase RelacionAdmin
    """
    list_display = ('ItemOrigen', 'TipoRelacion', 'ItemDestino',)
    list_filter = ('ItemOrigen', 'TipoRelacion', 'ItemDestino',)
    search_fields = ['ItemOrigen']
    ordering = ('ItemOrigen', 'ItemDestino',)


class AtributoItemAdmin(admin.ModelAdmin):
    """
    Definicion de la clase AtributoItemAdmin
    """
    list_display = ('Nombre', 'Item', 'AtributoTipoItem', 'Descripcion',)
    list_filter = ( 'Item', 'AtributoTipoItem',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)


class AtributoItemAdmin2(admin.TabularInline):
    """
    Definicion de la clase AtributoItemAdmin2 que se utiliza para la clase ItemAdmin
    """
    ordering = ('Nombre',)
    model = AtributoItem
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    """
    Definicion de la clase ItemAdmin
    """
    list_display = (
    'Nombre', 'TipoItem', 'Descripcion', 'Complejidad', 'Estado', 'Version', 'Costo', 'FechaModificacion',)
    list_filter = ( 'TipoItem', 'Complejidad', 'Estado', 'Costo', 'FechaModificacion',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)
    inlines = [AtributoItemAdmin2]


class ItemAdmin2(admin.TabularInline):
    """
    Definicion de la clase ItemAdmin2 que se utiliza para la clase FaseAdmin
    """
    ordering = ('Nombre',)
    model = Item
    extra = 0



class AtributoTipoItemAdmin(admin.ModelAdmin):
    """
    Definicion de la clase AtributoTipoItemAdmin
    """
    list_display = ('Nombre', 'TipoItem', 'Descripcion',)
    list_filter = ( 'TipoItem',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)


class AtributoTipoItemAdmin2(admin.TabularInline):
    """
    Definicion de la clase AtributoTipoItemAdmin2 que se utiliza para la clase TipoItemAdmin
    """
    ordering = ('Nombre',)
    model = AtributoTipoItem
    extra = 0


class TipoItemAdmin(admin.ModelAdmin):
    """
    Definicion de la clase TipoItemAdmin
    """
    list_display = ('Nombre', 'Fase', 'Descripcion',)
    list_filter = ( 'Fase',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)
    inlines = [ItemAdmin2, AtributoTipoItemAdmin2]


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
    list_display = ('Nombre', 'Descripcion', 'FechaCreacion', 'FechaInicio', 'FechaFin',)
    list_filter = ( 'FechaCreacion', 'FechaInicio', 'Estado',)
    search_fields = ['Nombre']
    ordering = ('Nombre',)
    inlines = [FaseAdmin2]


admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Fase, FaseAdmin)
admin.site.register(TipoItem, TipoItemAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(RelacionItem, RelacionAdmin)
admin.site.register(AtributoTipoItem, AtributoTipoItemAdmin)
admin.site.register(AtributoItem, AtributoItemAdmin)
admin.site.register(LineaBase, LineaBaseAdmin)