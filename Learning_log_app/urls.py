"""Defines URL patterns for the Learning_log_app"""
from django.urls import path
from .views import index, homepage, topics, topic

app_name = "Learning_log_app"
urlpatterns = [
    # Parent Home page
    path('', homepage, name='homepage'),
    # App Home page
    path('index/', index, name='index'),
    # Topics page
    path('topics/', topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', topic, name='topic'),

]
