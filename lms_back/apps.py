from django.apps import AppConfig


class LmsBackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lms_back'

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'