"""Defines URL patterns for the Learning_log_app"""
from django.urls import path
from .views import index

app_name = "Learning_log_app"
urlpatterns = [
    # Home page
    path('', index, name='index'),
]
