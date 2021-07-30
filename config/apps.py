# this code (from line 2 to 7), has been copied at /app/apps.py
# was changed the name = 'config' by name = 'app'
# and accessed from settings.py INSTALLED_APPS = {'app.apps.ConfigConfig'}
from django.apps import AppConfig


class ConfigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'config'

