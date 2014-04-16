from django.contrib import admin

from models import *

#Testcomentario
class FaseAdmin(admin.TabularInline):
    model = Fase
    extra = 0


class ProyectoAdmin(admin.ModelAdmin):
    inlines = [FaseAdmin]


admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Fase)
