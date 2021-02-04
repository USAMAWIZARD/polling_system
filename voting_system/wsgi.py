"""
WSGI config for voting_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voting_system.settings')

application = get_wsgi_application()


from django_socketio.views import sio
import socketio

application = socketio.WSGIApp(sio, application)

import eventlet
import eventlet.wsgi

eventlet.wsgi.server(eventlet.listen(('', 8000)), application)