"""Defines URL patterns for the Learning_log_app"""
from django.urls import path
from .views import index, homepage

app_name = "Learning_log_app"
urlpatterns = [
    # Parent Home page
    path('', homepage, name='homepage'),

    # App Home page
    path('index/', index, name='index'),

]
