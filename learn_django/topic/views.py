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
    viewed_topics = request.session.get('viewed_topics', set())
    topic = get_object_or_404(Topic, slug=in_slug)

    # TODO: Post Auth Support, tie like, view to users
    if topic.slug not in viewed_topics:
        viewed_topics.add(topic.slug)
        topic.metadata.viewed()
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


def find_topic(request):
    if request.method == 'POST':
        if 'query' in request.POST:
            # TODO: Clean Form input
            in_query = str(request.POST['query']).strip()
            topics = Topic.objects.filter(title__icontains=in_query)
            return render(
                request,
                'topic/find_topic.html',
                {
                    'topics': topics,
                    'user_query': in_query
                }
            )
        else:
            return redirect('home')
    else:
        # TODO: Handle method not allowed error
        return redirect('home')
