from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form"""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("username", "email", "age", "city", "state")


class CustomUserChangeForm(UserChangeForm):
    """Custom user change form"""

    class Meta:
        model = CustomUser
        fields = ("username", "email", "age", "city", "state")
