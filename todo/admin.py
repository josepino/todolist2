from django.contrib import admin

from models import *

#Testcomentario
class FaseAdmin(admin.TabularInline):
    list_display = ('Nombre',)
    list_filter = ('Nombre',)
    search_fields = ['Nombre']
    model = Fase
    extra = 0


class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)
    list_filter = ('Nombre',)
    search_fields = ['Nombre']
    inlines = [FaseAdmin]


#admin.site.register(Proyecto, ProyectoAdmin)
#admin.site.register(Fase)
admin.site.register(Proyecto)
