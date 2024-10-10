from django.contrib import admin
from .models import Topic, TopicMeta


# Register your models here.
admin.site.register(Topic)
admin.site.register(TopicMeta)
