from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Topic, TopicMeta


@receiver(post_save, sender=Topic)
def create_topic_metadata(sender, instance, created, **kwargs):
    """
    On Topic-created signal, create and map the metadata instance to the Topic instance
    """
    # TODO: Auto-create is broken
    if created:
        TopicMeta.objects.create(topic=instance)
