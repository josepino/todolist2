from django.shortcuts import render_to_response, get_object_or_404

from django.template import RequestContext

from todo.models import *


def index(request):
    todo = Proyecto.objects.all().order_by('id')  #select * from Todos
    return render_to_response('index.html', RequestContext(request, locals()))


def ver_fase(request, id):
    ver = get_object_or_404(Proyecto, id=id)
    return render_to_response('todo/ver.html', RequestContext(request, locals()))

#Create your views here.
