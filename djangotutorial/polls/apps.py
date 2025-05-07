# I am importing the AppConfig class from the django.apps module
from django.apps import AppConfig

# the PollsCnonfig class is a subclass of the AppConfig class
class PollsConfig(AppConfig):
    # default_auto_field is a string that defines the default auto field type for the app
    # I am setting the default_auto_field to BigAutoField, which is a 64-bit integer field
    # that automatically increments its value
    default_auto_field = 'django.db.models.BigAutoField'
    # the name variable is set to 'polls' which is the name of the app
    name = 'polls'
