from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)
