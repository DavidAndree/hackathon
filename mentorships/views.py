from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from accounts.models import Mentee, Mentor


class ConfigureRoleView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user

        # Ensure user is a mentee by default
        mentee, created = Mentee.objects.get_or_create(user=user)

        if Mentor.objects.filter(user=user).exists():
            return redirect(reverse("mentor_dashboard"))  # Redirect to mentor dashboard

        return render(request, "mentorship/configure_role.html")

    def post(self, request):
        return redirect(
            reverse("subscribe_mentor")
        )  # Redirect to mentor subscription flow


class MenteeDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        mentors = Mentor.objects.all()  # Fetch all mentors
        return render(request, "mentorship/menteedashboard.html", {"mentors": mentors})


class MentorDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        if not Mentor.objects.filter(user=request.user).exists():
            return redirect(reverse("mentee_dashboard"))  # Redirect non-mentors

        mentees = Mentee.objects.all()  # Fetch all mentees
        return render(request, "mentorship/mentor_dashboard.html", {"mentees": mentees})
