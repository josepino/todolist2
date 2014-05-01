from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()
#Definicion de la forma de las URLs
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todolist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'signups.views.home', name='home'),
    #url(r'^', include(todo.urls)),
    url(r'^admin/', include(admin.site.urls)),
)