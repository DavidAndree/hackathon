from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CustomUserCreationForm


class SignupView(CreateView):
    """Signup view"""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("configure_role")
    template_name = "registration/signup.html"


class TestView(ListView):

    success_url = reverse_lazy("test_template")
    template_name = "test_template.html"
