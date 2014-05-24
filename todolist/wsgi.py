"""
WSGI config for todolist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
#El primero se ha comentado por que se uso para probar
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todolist.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
