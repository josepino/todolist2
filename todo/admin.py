from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from models import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django import forms
from django.shortcuts import render_to_response, render
from django.contrib.auth.signals import user_logged_in

"""class FilterUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def queryset(self, request):
        qs = super(FilterUserAdmin, self).queryset(request)
        return qs.filter(created_by=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            # the changelist itself
            return True
        return obj.user === request.user"""


class SolicitudItemAdmin(admin.ModelAdmin):
    """
    Definicion de la clase RelacionAdmin
    """
    list_display = ('item', 'costo', 'complejidad', 'votos', 'votossi', 'votosno', 'solicitante',)
    list_filter = ('item', 'costo', 'complejidad', 'votos', 'solicitante',)
    search_fields = ['item']
    ordering = ('item',)
    readonly_fields = ('item', 'costo', 'complejidad', 'votos', 'votossi', 'votosno', 'completo', 'solicitante',)
    actions = ('votar',)

    class VotoForm(forms.Form):
        """
        Definicion del formulario ImportarTipoForm
        """
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
        #item = forms.ModelChoiceField(queryset=RelacionItem.objects.filter(itemorigen=id_item), initial=1)

        class Meta:
            model = Item

    def votar(self, request, queryset):
        """
        Definicion de la accion solicitar_cambio
        """
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)

        count = 0
        cont = 0
        ban = 0
        for a in queryset:
            count += 1
        if count == 1:
            for a in queryset:
                id_proyecto = a.item.tipoitem.fase.fkproyecto.id
                comit = Comite.objects.get(proyecto_id=id_proyecto)
                miembros1 = comit.miembros.all()
                for m in miembros1:
                    cont = cont + 1
                for miembro in miembros1:
                    if request.user.id == miembro.id:
                        ban = ban + 1
                        if cont == a.votos:
                            messages.error(request, "Ya se realizaron todos los votos para esta solicitud.")
                        else:
                            form = None
                            #admin.ModelAdmin.message_user(request,"Se realizo la solicitud del cambio en el item.")
                            if 'apply' in request.POST:
                                form = self.VotoForm(request.POST)

                                if form.is_valid():
                                    item = form.cleaned_data['Item']
                                    count = 0
                                    #for fase in queryset:
                                    #   fase.tipoitem.add(tipoitem)
                                    #  count += 1
                                    plural = ''
                                    if count != 1:
                                        plural = 's'

                                    self.message_user(request, "Successfully added tag %s to %d article%s." % (
                                    item, count, plural))
                                    return HttpResponseRedirect(request.get_full_path())

                            if not form:
                                form = self.VotoForm(
                                    initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
                            return render_to_response('admin/voto.html', {'item': a.item,
                                                                          'item_form': form,
                                                                          'id_solicitud': a.id,
                                                                          'costo': a.costo,
                                                                          'complejidad': a.complejidad,
                            })
                if ban == 0:
                    messages.error(request,
                                   "No puede votar en esta solicitud ya que no es miembro del comite de cambio de este item.")
        else:
            messages.error(request, "Solo se puede votar el cambio de un item a la vez.")

    votar.short_description = "Votar para el cambio del Item"

    """def queryset(self, request):
        qs = super(SolicitudItemAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs

        # get instructor's "owner"
        return qs.filter(instructor__owner=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "instructor" and not request.user.is_superuser:
            kwargs["queryset"] = Instructor.objects.filter(owner=request.user)
            return db_field.formfield(**kwargs)
        return super(CourseAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def queryset(self, request):
        qs = super(FilterUserAdmin, self).queryset(request)
        return qs.filter(created_by=request.user)


    def queryset(self, request):
        qs = super(SolicitudItemAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author = request.user)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True # So they can see the change list page
        if request.user.is_superuser or obj.author == request.user:
            return True
        else:
            return False

    has_delete_permission = has_change_permission"""


class RelacionAdmin(admin.ModelAdmin):
    """
    Definicion de la clase RelacionAdmin
    """
    list_display = ('itemorigen', 'tiporelacion', 'itemdestino',)
    list_filter = ('itemorigen', 'tiporelacion', 'itemdestino',)
    search_fields = ['itemorigen']
    ordering = ('itemorigen', 'itemdestino',)


class ComiteAdmin(admin.ModelAdmin):
    """
    Definicion de la clase Comitedmin
    """
    list_display = ('proyecto', 'lista_miembros',)
    list_filter = ('miembros',)
    search_fields = ['proyecto']
    ordering = ('proyecto',)

    def lista_miembros(self, obj):
        return "\n|\n".join([p.username for p in obj.miembros.all()])


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
        'nombre', 'tipoitem', 'descripcion', 'complejidad', 'estado', 'version', 'costo', 'fechamodificacion',
        'complejidadtotal', 'costototal',)
    list_filter = ( 'tipoitem', 'complejidad', 'estado', 'costo', 'fechamodificacion',)
    search_fields = ['nombre']
    ordering = ('nombre',)
    inlines = [AtributoItemAdmin2]
    readonly_fields = ('complejidadtotal', 'costototal', 'idversion')
    actions = ('calcular_impacto', 'revertir_version', 'solicitar_cambio',)

    def calcular_impacto(modeladmin, request, queryset):
        """
        Definicion de la accion calcular_impacto
        """

        def impacto_complejidad(id_item):
            """ Recibe un request, se verifica cual es el usuario registrado y el proyecto del cual se solicita,
            se obtiene la lista de fases con las que estan relacionados el usuario y el proyecto
            desplegandola en pantalla, ademas permite realizar busquedas avanzadas sobre
            las fases que puede mostrar.


            """
            item = Item.objects.get(id=id_item)
            com = 0
            try:
                relaciones = RelacionItem.objects.filter(itemorigen=id_item)
            except RelacionItem.DoesNotExist:
                relaciones = False
            if relaciones:
                for hijo in relaciones:
                    com = com + impacto_complejidad(hijo.itemdestino.id)
                com = com + item.complejidad
                return com
            else:
                return item.complejidad

        def impacto_costo(id_item):
            """ Recibe un request, se verifica cual es el usuario registrado y el proyecto del cual se solicita,
            se obtiene la lista de fases con las que estan relacionados el usuario y el proyecto
            desplegandola en pantalla, ademas permite realizar busquedas avanzadas sobre
            las fases que puede mostrar.

            """
            item = Item.objects.get(id=id_item)
            cost = 0
            try:
                relaciones = RelacionItem.objects.filter(itemorigen=id_item)
            except RelacionItem.DoesNotExist:
                relaciones = False
            if relaciones:
                for hijo in relaciones:
                    cost = cost + impacto_costo(hijo.itemdestino.id)
                cost = cost + item.costo
                return cost
            else:
                return item.costo

        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        count = 0
        for a in queryset:
            count += 1

        if count == 1:
            for a in queryset:
                item1 = Item.objects.get(id=a.id)
                item1.complejidadtotal = impacto_complejidad(a.id)
                item1.costototal = impacto_costo(a.id)
                item1.save()
                #super(Item, item1).save()
                modeladmin.message_user(request,
                                        "Se calculo correctamente correctamente impaco del cambio en el item %s." % item1)
        else:
            messages.error(request, "Solo se puede calcular el impacto de un item a la vez.")
    calcular_impacto.short_description = "Calcular Impacto del Item"

    def revertir_version(modeladmin, request, queryset):
        """
        Definicion de la accion calcular_impacto
        """
        count = 0
        idite = 0
        for a in queryset:
            count += 1

        if count == 1:
            for a in queryset:
                items = Item.objects.filter(idversion=a.id)
                if a.version > 1:
                    for b in items:
                        if b.version == (a.version - 1):
                            idite == b.id
                            atributos = AtributoItem.objects.all()
                            for at in atributos:
                                if at.item.id == a.id:
                                    new = AtributoItem()
                                    new.nombre = at.nombre
                                    new.descripcion = at.descripcion
                                    new.item = b
                                    new.atributotipoitem = at.atributotipoitem
                                    new.save()
                            relaciones1 = RelacionItem.objects.all()
                            for rel1 in relaciones1:
                                if rel1.itemorigen.id == a.id:
                                    new1 = RelacionItem()
                                    new1.itemorigen = b
                                    new1.tiporelacion = rel1.tiporelacion
                                    new1.itemdestino = rel1.itemdestino
                                    new1.save()
                            relaciones2 = RelacionItem.objects.all()
                            for rel2 in relaciones2:
                                if rel2.itemdestino.id == a.id:
                                    new2 = RelacionItem()
                                    new2.itemorigen = rel2.itemorigen
                                    new2.tiporelacion = rel2.tiporelacion
                                    new2.itemdestino = b
                                    new2.save()
                            items1 = Item.objects.filter(idversion=a.id)
                            for b1 in items1:
                                b1.idversion = b.id
                                b1.save()
                            messages.info(request, "Se realizo correctamente la version del item %s ." % a)
                            a.delete()

                else:
                    messages.error(request, "No existe una version anterior del item.")

        else:
            messages.error(request, "Solo se puede revertir la version de un item a la vez.")

    revertir_version.short_description = "Revertir version del Item"

    class SolicitarCambioForm(forms.Form):
        """
        Definicion del formulario ImportarTipoForm
        """
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
        #item = forms.ModelChoiceField(queryset=RelacionItem.objects.filter(itemorigen=id_item), initial=1)

        class Meta:
            model = Item

    def solicitar_cambio(self, request, queryset):
        """
        Definicion de la accion solicitar_cambio
        """
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)

        count = 0
        for a in queryset:
            count += 1
        if count == 1:
            id_item = (",".join(selected))
            form = None
            it = Item.objects.get(id=id_item)
            if it.estado == 'A':
                #admin.ModelAdmin.message_user(request,"Se realizo la solicitud del cambio en el item.")
                if 'apply' in request.POST:
                    form = self.SolicitarCambioForm(request.POST)

                    if form.is_valid():
                        item = form.cleaned_data['Item']
                        count = 0
                        #for fase in queryset:
                        #   fase.tipoitem.add(tipoitem)
                        #  count += 1
                        plural = ''
                        if count != 1:
                            plural = 's'

                        self.message_user(request, "Successfully added tag %s to %d article%s." % (item, count, plural))
                        return HttpResponseRedirect(request.get_full_path())

                if not form:
                    form = self.SolicitarCambioForm(
                        initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
                return render_to_response('admin/ConfirmarSolicitud.html', {'item': queryset,
                                                                            'item_form': form,
                                                                            'id_item': id_item,
                })
            else:
                messages.error(request, "No se puede solicitar el cambio de un item que no este en estado 'Aprobado'.")
        else:
            messages.error(request, "Solo se puede solicitar el cambio de un item a la vez.")

    solicitar_cambio.short_description = "Solicitar cambio del item"


class ItemAdmin2(admin.TabularInline):
    """
    Definicion de la clase ItemAdmin2 que se utiliza para la clase FaseAdmin
    """
    ordering = ('nombre',)
    model = Item
    extra = 0


class ItemAdmin3(admin.TabularInline):
    """
    Definicion de la clase ItemAdmin2 que se utiliza para la clase FaseAdmin
    """
    ordering = ('nombre',)
    fields = ('nombre', 'descripcion')
    model = Item
    extra = 0


class LineaBaseAdmin(admin.ModelAdmin):
    """
    Definicion de la clase LineaBaseAdmin
    """
    list_display = ('nombre', 'fase', 'fechacreacion', 'estado',)
    list_filter = ( 'fase', 'fechacreacion', 'estado',)
    search_fields = ['nombre']
    ordering = ('nombre',)
    inlines = [ItemAdmin3]


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
    actions = ('iniciar_fase', 'finalizar_fase', 'ImportarTipo',)
    inlines = [TipoItemAdmin2]

    def iniciar_fase(modeladmin, request, queryset):
        """
        Definicion de la accion iniciar_fase
        """
        rows_updated = queryset.update(fechainicio=datetime.datetime.now())
        if rows_updated == 1:
            message_bit = "1 fase fue iniciada"
        else:
            message_bit = "%s fases fueron iniciadas" % rows_updated
        modeladmin.message_user(request, "%s correctamente." % message_bit)

    iniciar_fase.short_description = "Iniciar la fase seleccionada"

    def finalizar_fase(modeladmin, request, queryset):
        """
        Definicion de la accion finalizar_fase
        """
        rows_updated = queryset.update(fechafin=datetime.datetime.now())

        if rows_updated == 1:
            message_bit = "1 fase fue finalizada"
        else:
            message_bit = "%s fases fueron finalizadas" % rows_updated
        modeladmin.message_user(request, "%s correctamente." % message_bit)

    finalizar_fase.short_description = "Finalizar la fase seleccionada"

    def importar_tipoitem(modeladmin, request, queryset):
        """
        Definicion de la accion importar_tipoitem
        """
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        count = 0
        for a in queryset:
            count += 1
        if count == 1:
            return HttpResponseRedirect('/importartipoitem/%s/1' % (",".join(selected)))
        else:
            messages.error(request, "Solo se puede importar Tipo de Item en una fase a la vez.")

    importar_tipoitem.short_description = "Importar tipo de Item22"

    class ImportarTipoForm(forms.Form):
        """
        Definicion del formulario ImportarTipoForm
        """
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
        tipoitem = forms.ModelChoiceField(queryset=TipoItem.objects.all(), initial=1)

        class Meta:
            model = TipoItem

    def ImportarTipo(self, request, queryset):
        """
        Definicion de la accion ImportarTipo
        """
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)

        count = 0
        for a in queryset:
            count += 1
        if count == 1:
            id_fase = (",".join(selected))
            form = None
            tipoitem = None
            if 'apply' in request.POST:
                form = self.ImportarTipoForm(request.POST)

                if form.is_valid():
                    tipoitem = form.cleaned_data['TipoItem']
                    count = 0
                    for fase in queryset:
                        fase.tipoitem.add(tipoitem)
                        count += 1
                    plural = ''
                    if count != 1:
                        plural = 's'

                    self.message_user(request, "Successfully added tag %s to %d article%s." % (tipoitem, count, plural))
                    return HttpResponseRedirect(request.get_full_path())

            if not form:
                form = self.ImportarTipoForm(
                    initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
            return render_to_response('admin/ImportarTipo.html', {'fase': queryset,
                                                                  'tipoitem_form': form,
                                                                  'id_fase': id_fase,
                                                                  'tipoitem': tipoitem,
            })
        else:
            messages.error(request, "Solo se puede importar Tipo de Item en una fase a la vez.")

    ImportarTipo.short_description = "Importar tipo de Item"


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
    actions = ('iniciar_proyecto', 'finalizar_proyecto', 'Informes',)
    inlines = [FaseAdmin2]

    def iniciar_proyecto(modeladmin, request, queryset):
        """
        Definicion de la accion iniciar_proyecto
        """
        rows_updated = queryset.update(fechainicio=datetime.datetime.now())
        if rows_updated == 1:
            message_bit = "1 proyecto fue iniciado"
        else:
            message_bit = "%s proyectos fueron iniciados" % rows_updated
        modeladmin.message_user(request, "%s correctamente." % message_bit)

    iniciar_proyecto.short_description = "Iniciar el proyecto seleccionado"

    def finalizar_proyecto(modeladmin, request, queryset):
        """
        Definicion de la accion finalizar_proyecto
        """
        rows_updated = queryset.update(fechafin=datetime.datetime.now())
        if rows_updated == 1:
            message_bit = "1 proyecto fue finalizado"
        else:
            message_bit = "%s proyectos fueron finalizados" % rows_updated
        modeladmin.message_user(request, "%s correctamente." % message_bit)

    finalizar_proyecto.short_description = "Finalizar el proyecto seleccionado"

    class InformeForm(forms.Form):
        """
        Definicion del formulario InformeForm
        """
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)

        class Meta:
            model = Proyecto

    def Informes(self, request, queryset):
        """
        Definicion de la accion  InformeSolicitudes
        """
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)

        count = 0
        for a in queryset:
            count += 1
        if count == 1:
            id_proyecto = (",".join(selected))
            form = None
            if 'apply' in request.POST:
                form = self.InformeForm(request.POST)

                if form.is_valid():
                    count = 0
                    for proyecto in queryset:
                        count += 1
                    plural = ''
                    if count != 1:
                        plural = 's'

                    self.message_user(request, "Successfully added tag %s to %d article%s." % (tipoitem, count, plural))
                    return HttpResponseRedirect(request.get_full_path())

            if not form:
                form = self.InformeForm(
                    initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
            proyecto = Proyecto.objects.get(id=id_proyecto)
            return render_to_response('admin/reporte.html', {'proyecto': proyecto,
                                                             'id_proyecto': id_proyecto,
            })
        else:
            messages.error(request, "Solo se puede realizar el informe de un proyecto a la vez.")

    Informes.short_description = "Realizar informes"


def logged_in_message(sender, user, request, **kwargs):
    sol = SolicitudItem.objects.all()
    for s in sol:
        if s.completo <> True:
            id_proyecto = s.item.tipoitem.fase.fkproyecto.id
            comit = Comite.objects.get(proyecto_id=id_proyecto)
            miembros1 = comit.miembros.all()
            for m in miembros1:
                if m.id == request.user.id:
                    messages.info(request, "Tiene una solicitud Pendiente de cambio!!!")


user_logged_in.connect(logged_in_message)

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Fase, FaseAdmin)
admin.site.register(TipoItem, TipoItemAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(RelacionItem, RelacionAdmin)
admin.site.register(AtributoTipoItem, AtributoTipoItemAdmin)
admin.site.register(AtributoItem, AtributoItemAdmin)
admin.site.register(LineaBase, LineaBaseAdmin)
admin.site.register(SolicitudItem, SolicitudItemAdmin)
admin.site.register(Comite, ComiteAdmin)