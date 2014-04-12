from django.contrib import admin
from models import *

class TodoArticuloAdmin(admin.TabularInline):
	model = TodoArticulo
	extra = 0


class TodoAdmin(admin.ModelAdmin):
	inlines = [TodoArticuloAdmin]


#admin.site.register (Todo, TodoAdmin)
#admin.site.register (TodoArticulo)
