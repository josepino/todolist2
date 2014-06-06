from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from todo.models import *
from django.db import IntegrityError


def index(request):
    """
    Definimos el view index
    """
    return render_to_response('todo/index.html')


#def index(request):
#    todo = Proyecto.objects.all().order_by('id')  #select * from Todos
#    return render_to_response('todo/index.html', RequestContext(request, locals()))


def ver_fase(request, id):
    """
    Definimos el view ver_fase
    """
    ver = get_object_or_404(Proyecto, id=id)
    return render_to_response('todo/ver.html', RequestContext(request, locals()))


def ImportarTipoItem(request, id_fase, id_tipoitem):
    """
    Definimos el view ImportarTipoItem
    """
    tipoItemExistente = TipoItem.objects.get(id=id_tipoitem)
    tipoItemNuevo = TipoItem.objects.get(id=id_tipoitem)
    fase = Fase.objects.get(id=id_fase)

    tipoItemNuevo.id = None
    tipoItemNuevo.fase = fase
    try:
        tipoItemNuevo.save()
    except IntegrityError as e:
        return render(request, "keyduplicate_tipoitem.html",
                      {'fase': fase, 'tipoitem': tipoItemNuevo, "message": e.message},
                      context_instance=RequestContext(request))

    atributos = AtributoTipoItem.objects.filter(tipoitem=tipoItemExistente)
    for atributo in atributos:
        atributo.id = None
        atributo.tipoitem = tipoItemNuevo
        atributo.save()
    return HttpResponseRedirect('/admin/todo/tipoitem/' + str(tipoItemNuevo.id))


def SolicitarCambio(request, id_item):
    """
    Definimos el view SolicitarCambio
    """
    #tipoItemExistente = TipoItem.objects.get(id=id_tipoitem)
    #tipoItemNuevo = TipoItem.objects.get(id=id_tipoitem)
    item = Item.objects.get(id=id_item)

    #tipoItemNuevo.id = None
    #tipoItemNuevo.fase = fase
    try:
        item.calcular_impacto()
    except IntegrityError as e:
        return render(request, "keyduplicate_tipoitem.html",
                      {'item': item, "message": e.message},
                      context_instance=RequestContext(request))

    item.estado = 'V'
    super(Item, item).save()
    solicitud = SolicitudItem()
    solicitud.item = item
    solicitud.complejidad = item.complejidadtotal
    solicitud.costo = item.costototal
    solicitud.votos = 0
    solicitud.votossi = 0
    solicitud.votosno = 0
    solicitud.save()
    return HttpResponseRedirect('/admin/todo/solicituditem/')


def VotoSi(request, id_solicitud):
    """
    Definimos el view VotoSi
    """
    #tipoItemExistente = TipoItem.objects.get(id=id_tipoitem)
    #tipoItemNuevo = TipoItem.objects.get(id=id_tipoitem)
    solicitud = SolicitudItem.objects.get(id=id_solicitud)
    solicitud.votos = solicitud.votos + 1
    solicitud.votossi = solicitud.votossi + 1
    solicitud.save()
    return HttpResponseRedirect('/admin/todo/solicituditem/')


def VotoNo(request, id_solicitud):
    """
    Definimos el view VotoNo
    """
    #tipoItemExistente = TipoItem.objects.get(id=id_tipoitem)
    #tipoItemNuevo = TipoItem.objects.get(id=id_tipoitem)
    solicitud = SolicitudItem.objects.get(id=id_solicitud)
    solicitud.votos = solicitud.votos + 1
    solicitud.votosno = solicitud.votosno + 1
    solicitud.save()
    return HttpResponseRedirect('/admin/todo/solicituditem/')


def ListarTipoItem(request, id_fase):
    """
    Definimos el view ListarTipoItem
    """
    tipoitem_fase = TipoItem.objects.filter(fase=id_fase)
    tipoitem_available = tipoitem_fase.values_list('id', flat=True)
    tipoitem = TipoItem.objects.exclude(pk__in=tipoitem_available)

    fase = Fase.objects.get(pk=id_fase)
    projecto = fase.fkproyecto
    return render(request, "listartipoitem.html",
                  {'user': request.user, 'itemtypes': tipoitem, 'id_fase': id_fase, 'project': projecto})


def CalcularImpacto(request, id_item):
    """
    Definimos el view CalcularImpacto
    """
    item = Item.objects.get(id=id_item)

    item.complejidadtotal = impacto_complejidad(id_item)
    item.costototal = impacto_costo(id_item)
    item.save()
    return HttpResponseRedirect('/admin/todo/item')


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


"""
def calcular_items_afectados(id_item):
    "" Recibe un request, se verifica cual es el usuario registrado y el proyecto del cual se solicita,
    se obtiene la lista de fases con las que estan relacionados el usuario y el proyecto
    desplegandola en pantalla, ademas permite realizar busquedas avanzadas sobre
    las fases que puede mostrar.


    ""
    item = Items.objects.get(id=id_item)
    lista_hijos = []
    try:
        hijos = Items.objects.filter(padre=id_item)
    except Items.DoesNotExist:
        hijos = False
    if hijos:
        for hijo in hijos:
            lista_hijos.extend(calcular_items_afectados(hijo.id))
        lista_hijos.append(item)
        return lista_hijos
    else:
        lista_hijos.append(item)
        return lista_hijos

            """
