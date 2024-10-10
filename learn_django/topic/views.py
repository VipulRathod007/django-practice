from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Topic


# Create your views here.
def topics(request):
    topics = Topic.objects.all()
    return render(request, 'topic/topics.html', {'topics': topics})


def topic(request, in_slug: str):
    # TODO: Parse slug for injection?
    # TODO: Implement View/Like event
    topic = get_object_or_404(Topic, slug=in_slug)
    return render(request, 'topic/topic.html', {'topic': topic})
