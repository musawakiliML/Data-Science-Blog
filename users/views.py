from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    """Register a New User"""
    if request.method != "POST":
        # Display blank registration form
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Login redirect to home page
            login(request, new_user)
            return redirect('Learning_log_app:index')

    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'register.html', context)
