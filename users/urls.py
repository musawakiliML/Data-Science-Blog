"""Defines URL patterns for users"""

from django.urls import path, include

from .views import register  # profile

# name of the auth app
app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', register, name='register'),

    # Profile Page
    #path('profile/<int:user_id>', profile, name='profile'),
]
