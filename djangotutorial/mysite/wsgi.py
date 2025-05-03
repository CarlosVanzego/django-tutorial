"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
# this import is used to set the default value for the DJANGO_SETTINGS_MODULE environment variable, similar to the asgi.py file
import os
# this line is importing the get_wsgi_application function from the django.core.wsgi module
from django.core.wsgi import get_wsgi_application
# os.environ.setdefault is used to set the default value for the DJANGO_SETTINGS_MODUEL environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# application is set to the result of calling get_wsgi_application
application = get_wsgi_application()
