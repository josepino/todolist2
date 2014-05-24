from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from todo.models import *
from django.db import IntegrityError


def index(request):
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
