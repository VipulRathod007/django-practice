from django.apps import AppConfig


class TopicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'topic'

    def ready(self):
        from .signals import create_topic_metadata
