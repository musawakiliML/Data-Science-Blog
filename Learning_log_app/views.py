from django.shortcuts import render

# Create your views here.


def index(request):
    """The home page for the learning log app"""
    return render(request, 'index.html')
