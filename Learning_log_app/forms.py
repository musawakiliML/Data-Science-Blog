from statistics import mode
from django import forms
from .models import Topic


# Create your forms
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': 'enter topic here..'}
