from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .forms import CustomUserCreationForm
from .models import CustomUser


class SignupView(CreateView):
    """Signup view"""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("configure_role")
    template_name = "registration/signup.html"


class TestView(ListView):

    success_url = reverse_lazy("test_template")
    template_name = "test_template.html"


class UserListView(ListView):
    model = CustomUser
    template_name = "user_list.html"


class UserDetailView(DetailView):
    model = CustomUser
    template_name = "user_detail.html"
