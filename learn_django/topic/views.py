from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from .models import Topic
from .forms import TopicForm


# Create your views here.
def topics(request):
    topics = Topic.objects.all()
    return render(request, 'topic/topics.html', {'topics': topics})


def topic(request, in_slug: str):
    # TODO: Parse slug for injection?
    # TODO: Implement View/Like event
    topic = get_object_or_404(Topic, slug=in_slug)
    return render(request, 'topic/topic.html', {'topic': topic})


def create_topic(request):
    if request.method == 'POST':
        in_topicform = TopicForm(request.POST, request.FILES)
        if in_topicform.is_valid():
            in_topicform.clean()
            in_topicform.save()
            slug = Topic.objects.filter(slug=slugify(in_topicform.cleaned_data['title'])).first().slug
            return redirect('topic-detail', in_slug=slug)
        else:
            return render(request, 'topic/create-topic.html', {'topicform': in_topicform})
    elif request.method == 'GET':
        return render(request, 'topic/create-topic.html', {'topicform': TopicForm()})
