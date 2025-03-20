"""
WSGI config for meu_projeto_async project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# This code snippet is a WSGI (Web Server Gateway Interface) configuration for a Django project.
# Here's what each part does:
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_projeto_async.settings')
application = get_wsgi_application()
