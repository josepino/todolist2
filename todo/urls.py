from django.conf.urls import *
from .views import *
#Definimos como se veran las URLs
urlpatterns = patterns('todo.views',
                       url(r'^index/$', 'index', name='index'),
                       #url(r'^importartipoitem/(?P<id_fase>\d+)$', ListarTipoItem),
                       url(r'^importartipoitem/(?P<id_fase>\d+)/(?P<id_tipoitem>\d+)$', ImportarTipoItem),
                       url(r'^calcularimpacto/(?P<id_item>\d+)$', CalcularImpacto),
                       url(r'^solicitarcambio/(?P<id_item>\d+)$', SolicitarCambio),
                       url(r'^voto/si/(?P<id_solicitud>\d+)$', VotoSi),
                       url(r'^voto/no/(?P<id_solicitud>\d+)$', VotoNo),
                       #url(r'^revertir/(?P<id_item>\d+)$', RevertirItem),
)

