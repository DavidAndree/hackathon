from django.urls import path
from .views import ConfigureRoleView, MenteeDashboardView, MentorDashboardView

urlpatterns = [
    path('configure-role/', ConfigureRoleView.as_view(), name='configure_role'),
    path('mentee-dashboard/', MenteeDashboardView.as_view(), name='mentee_dashboard'),
    path('mentor-dashboard/', MentorDashboardView.as_view(), name='mentor_dashboard'),
]
