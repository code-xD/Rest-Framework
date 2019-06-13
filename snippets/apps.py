from django.apps import AppConfig
from django.db.models.signals import post_save


class SnippetsConfig(AppConfig):
    name = 'snippets'

    def ready(self):
        from .signals import send_notification
