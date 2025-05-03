"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""
# this is a configuration file for the Django ASGO server
# it is importing the os module to set the environment variable
import os
# this line is importing the get_asgi_application function from the django.core.asgi module
from django.core.asgi import get_asgi_application
# os.environ.setdefault is used to set the default value for the DJANGO_SETTINGS_MODULE environment variable
# mysite.settings is the settings module for the Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# the applicaiton variable is set to the result of calling get_asgi_application
application = get_asgi_application()
