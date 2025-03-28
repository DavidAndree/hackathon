from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Mentee, Mentor
from django.urls import reverse

@login_required
def configure_role(request):
    user = request.user
    
    # Ensure user is a mentee by default
    mentee, created = Mentee.objects.get_or_create(user=user)
    
    if Mentor.objects.filter(user=user).exists():
        return redirect(reverse('mentor_dashboard'))  # Redirect to mentor dashboard

    if request.method == "POST":
        return redirect(reverse('subscribe_mentor'))  # Redirect to mentor subscription flow

    return render(request, "mentorship/configure_role.html")

@login_required
def mentee_dashboard(request):
    mentors = Mentor.objects.all()  # Fetch all mentors
    return render(request, "mentorship/mentee_dashboard.html", {"mentors": mentors})

@login_required
def mentor_dashboard(request):
    if not Mentor.objects.filter(user=request.user).exists():
        return redirect(reverse('mentee_dashboard'))  # Redirect non-mentors
    
    mentees = Mentee.objects.all()  # Fetch all mentees
    return render(request, "mentorship/mentor_dashboard.html", {"mentees": mentees})