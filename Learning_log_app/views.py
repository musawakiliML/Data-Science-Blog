from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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
            return redirect('Learning_log_app:topics')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'new_topic.html', context)


def new_entry(request, topic_id):
    """Adding a new entry form"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data return empty form with a blank page
        form = TopicForm()
    else:
        # POST request submitted, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('Learning_log_app:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)


'''
def edit_entry(request, entry_id):
    """Edit An existing entry value."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if request.method != "POST":
        # Initial request; pre-fill form wth the current entry 
        form = EntryForm(instance=entry)
'''
