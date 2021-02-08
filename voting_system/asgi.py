"""
ASGI config for voting_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from voting_systemapp import views
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voting_system.settings')

django_application = get_asgi_application()

async def application(scope, receive, send):
    if scope['type'] == 'http':
        # Let Django handle HTTP requests
        await django_application(scope,receive, send)
    elif scope['type'] == 'websocket':
        await views.websocket_applciation(scope, receive, send)
        # We'll handle Websocket connections here
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")
