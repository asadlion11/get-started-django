from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_polls'
    label = 'polls'  # app label to use in migrations and admin site