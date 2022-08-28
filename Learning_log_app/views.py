from multiprocessing import context
from django.shortcuts import render
from .models import Topic, Entry

# Create your views here.


def index(request):
    """The home page for the learning log app"""
    return render(request, 'index.html')


def homepage(request):
    """Return Parent Homepage"""

    return render(request, 'base.html')


def topics(request):
    """Return Topics on the home page"""
    topics = Topic.objects.order_by("date_added")  # Topic.objects.all
    context = {'topics': topics}
    return render(request, 'topics.html', context)


def topic(request, topic_id):
    """Return single topic details"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)
