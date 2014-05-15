from django.contrib import admin

from models import *


class LineaBaseAdmin(admin.ModelAdmin):
    """
    Definicion de la clase LineaBaseAdmin
    """
    list_display = ('nombre', 'fase', 'fechacreacion', 'estado',)
    list_filter = ( 'fase', 'fechacreacion', 'estado',)
    search_fields = ['nombre']
    ordering = ('nombre',)


class RelacionAdmin(admin.ModelAdmin):
    """
    Definicion de la clase RelacionAdmin
    """
    list_display = ('itemorigen', 'tiporelacion', 'itemdestino',)
    list_filter = ('itemorigen', 'tiporelacion', 'itemdestino',)
    search_fields = ['itemorigen']
    ordering = ('itemorigen', 'itemdestino',)


class AtributoItemAdmin(admin.ModelAdmin):
    """
    Definicion de la clase AtributoItemAdmin
    """
    list_display = ('nombre', 'item', 'atributotipoitem', 'descripcion',)
    list_filter = ( 'item', 'atributotipoitem',)
    search_fields = ['nombre']
    ordering = ('nombre',)


class AtributoItemAdmin2(admin.TabularInline):
    """
    Definicion de la clase AtributoItemAdmin2 que se utiliza para la clase ItemAdmin
    """
    ordering = ('nombre',)
    model = AtributoItem
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    """
    Definicion de la clase ItemAdmin
    """
    list_display = (
        'nombre', 'tipoitem', 'descripcion', 'complejidad', 'estado', 'version', 'costo', 'fechamodificacion',)
    list_filter = ( 'tipoitem', 'complejidad', 'estado', 'costo', 'fechamodificacion',)
    search_fields = ['nombre']
    ordering = ('nombre',)
    inlines = [AtributoItemAdmin2]


class ItemAdmin2(admin.TabularInline):
    """
    Definicion de la clase ItemAdmin2 que se utiliza para la clase FaseAdmin
    """
    ordering = ('nombre',)
    model = Item
    extra = 0



class AtributoTipoItemAdmin(admin.ModelAdmin):
    """
    Definicion de la clase AtributoTipoItemAdmin
    """
    list_display = ('nombre', 'tipoitem', 'descripcion',)
    list_filter = ( 'tipoitem',)
    search_fields = ['nombre']
    ordering = ('nombre',)


class AtributoTipoItemAdmin2(admin.TabularInline):
    """
    Definicion de la clase AtributoTipoItemAdmin2 que se utiliza para la clase TipoItemAdmin
    """
    ordering = ('nombre',)
    model = AtributoTipoItem
    extra = 0


class TipoItemAdmin(admin.ModelAdmin):
    """
    Definicion de la clase TipoItemAdmin
    """
    list_display = ('nombre', 'fase', 'descripcion',)
    list_filter = ( 'fase',)
    search_fields = ['nombre']
    ordering = ('nombre',)
    inlines = [ItemAdmin2, AtributoTipoItemAdmin2]


class TipoItemAdmin2(admin.TabularInline):
    """
    Definicion de la clase TipoItemAdmin2 que se utiliza para la clase FaseAdmin
    """
    ordering = ('nombre',)
    model = TipoItem
    extra = 0


class FaseAdmin(admin.ModelAdmin):
    """
    Definicion de la clase FaseAdmin
    """
    list_display = ('nombre', 'fkproyecto', 'descripcion', 'fechacreacion',)
    list_filter = ( 'fkproyecto', 'fechacreacion', 'fechainicio', 'estado',)
    search_fields = ['nombre']
    ordering = ('nombre',)
    inlines = [TipoItemAdmin2]


class FaseAdmin2(admin.TabularInline):
    """
    Definicion de la clase FaseAdmin2 que se utiliza para la clase ProyectoAdmin
    """
    ordering = ('nombre',)
    model = Fase
    extra = 0


class ProyectoAdmin(admin.ModelAdmin):
    """
    Definicion de la clase ProyectoAdmin
    """
    list_display = ('nombre', 'descripcion', 'fechacreacion', 'fechainicio', 'fechafin',)
    list_filter = ( 'fechacreacion', 'fechainicio', 'estado',)
    search_fields = ['nombre']
    ordering = ('nombre',)
    inlines = [FaseAdmin2]


admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Fase, FaseAdmin)
admin.site.register(TipoItem, TipoItemAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(RelacionItem, RelacionAdmin)
admin.site.register(AtributoTipoItem, AtributoTipoItemAdmin)
admin.site.register(AtributoItem, AtributoItemAdmin)
admin.site.register(LineaBase, LineaBaseAdmin)