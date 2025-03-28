from django.urls import path
from .views import (
    ConfigureRoleView,
    MenteeDashboardView,
    MentorDashboardView,
    MentorConfigView,
)

urlpatterns = [
    path('configure-role/', ConfigureRoleView.as_view(), name='configure_role'),
    path('mentee-dashboard/', MenteeDashboardView.as_view(), name='mentee_dashboard'),
    path('mentor-dashboard/', MentorDashboardView.as_view(), name='mentor_dashboard'),
    path('mentor_config/', MentorConfigView.as_view(), name='mentor_config'),
]
