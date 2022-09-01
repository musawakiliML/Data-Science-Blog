from statistics import mode
from django import forms
from .models import Topic, Entry


# Create your forms
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry Text:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 100})}
