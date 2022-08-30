"""Defines URL patterns for users"""

from django.urls import path, include

# name of the auth app
app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
]
