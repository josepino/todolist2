from django.conf.urls import *
from .views import index
#Definimos como se veran las URLs
urlpatterns = patterns('todo.views',
                       url(r'^index/$', 'index', name='index'),
                       #url(r'^ver_fase/(?P<id>\d+)/$', 'ver_fase', name='ver'),
)



