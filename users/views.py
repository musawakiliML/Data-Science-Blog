from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.


def register(request):
    """Register a New User"""
    if request.method != "POST":
        # Display blank registration form
        #form = UserCreationForm()
        form = RegisterForm()
    else:
        # Process completed form
        #form = UserCreationForm(data=request.POST)
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Login redirect to home page
            login(request, new_user)
            return redirect('Learning_log_app:index')

    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logout(request):
    logout(request)
    return redirect('users:logout')


def profile(request, user_id):
    pass
