from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser  # Use CustomUser model


class ConfigureRoleView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user

        # Redirect mentor users to the mentor dashboard
        if user.is_mentor:
            return redirect(reverse("mentor_dashboard"))

        return render(request, "mentorship/configure_role.html")

    def post(self, request):
        return redirect(
            reverse("subscribe_mentor")
        )  # Redirect to mentor subscription flow


class MenteeDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        mentors = CustomUser.objects.filter(is_mentor=True)  # Fetch all mentors
        return render(request, "mentorship/menteedashboard.html", {"mentors": mentors})


class MentorDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user

        if not user.is_mentor:
            return redirect(reverse("mentee_dashboard"))  # Redirect non-mentors

        mentees = CustomUser.objects.filter(is_mentee=True)  # Fetch all mentees
        return render(request, "mentorship/mentor_dashboard.html", {"mentees": mentees})
    

class MentorConfigView(TemplateView):
    template_name = "mentorship/mentor_config.html"

