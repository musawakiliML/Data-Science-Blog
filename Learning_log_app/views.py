from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm

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


def new_topic(request):
    """Return new form to submit the topic to the data base"""
    if request.method != 'POST':
        # No data submitted, create a blank page.
        form = TopicForm()
    else:
        # POST submitted, process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'new_topic.html', context)
