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
    list_display = ('nombre', 'fkproyecto', 'descripcion', 'fechacreacion', 'fechainicio', 'fechafin',)
    list_filter = ( 'fkproyecto', 'fechacreacion', 'fechainicio', 'estado',)
    search_fields = ['nombre']
    ordering = ('nombre',)
    readonly_fields = ('fechainicio', 'fechafin',)
    actions = ('iniciar_fase', 'finalizar_fase',)
    inlines = [TipoItemAdmin2]

    def iniciar_fase(modeladmin, request, queryset):
        rows_updated = queryset.update(fechainicio=datetime.datetime.now())
        if rows_updated == 1:
            message_bit = "1 fase fue iniciada"
        else:
            message_bit = "%s fases fueron iniciadas" % rows_updated
        modeladmin.message_user(request, "%s correctamente." % message_bit)

    iniciar_fase.short_description = "Iniciar la fase seleccionado"

    def finalizar_fase(modeladmin, request, queryset):
        rows_updated = queryset.update(fechafin=datetime.datetime.now())
        if rows_updated == 1:
            message_bit = "1 fase fue finalizada"
        else:
            message_bit = "%s fases fueron finalizadas" % rows_updated
        modeladmin.message_user(request, "%s correctamente." % message_bit)

    finalizar_fase.short_description = "Finalizar la fase seleccionado"


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
    list_display = ('nombre', 'descripcion', 'fechacreacion', 'fechainicio', 'fechafin', )
    list_filter = ( 'fechacreacion', 'fechainicio', 'estado',)
    search_fields = ['nombre']
    readonly_fields = ('fechainicio', 'fechafin',)
    ordering = ('nombre',)
    fieldsets = (
        ('Nombre', {'fields': ('nombre', 'descripcion',)} ),
        ('Fechas', {'fields': ('fechacreacion', 'fechainicio', 'fechafin',)} ), ('Estado', {'fields': ('estado',)} ),)
    actions = ('iniciar_proyecto', 'finalizar_proyecto',)
    inlines = [FaseAdmin2]

    def iniciar_proyecto(modeladmin, request, queryset):
        rows_updated = queryset.update(fechainicio=datetime.datetime.now())
        if rows_updated == 1:
            message_bit = "1 proyecto fue iniciado"
        else:
            message_bit = "%s proyectos fueron iniciados" % rows_updated
        modeladmin.message_user(request, "%s correctamente." % message_bit)

    iniciar_proyecto.short_description = "Iniciar el proyecto seleccionado"

    def finalizar_proyecto(modeladmin, request, queryset):
        rows_updated = queryset.update(fechafin=datetime.datetime.now())
        if rows_updated == 1:
            message_bit = "1 proyecto fue finalizado"
        else:
            message_bit = "%s proyectos fueron finalizados" % rows_updated
        modeladmin.message_user(request, "%s correctamente." % message_bit)

    finalizar_proyecto.short_description = "Finalizar el proyecto seleccionado"


admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Fase, FaseAdmin)
admin.site.register(TipoItem, TipoItemAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(RelacionItem, RelacionAdmin)
admin.site.register(AtributoTipoItem, AtributoTipoItemAdmin)
admin.site.register(AtributoItem, AtributoItemAdmin)
admin.site.register(LineaBase, LineaBaseAdmin)