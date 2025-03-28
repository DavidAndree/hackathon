from django.urls import path
from .views import configure_role, mentee_dashboard, mentor_dashboard

urlpatterns = [
    path('configure-role/', configure_role, name='configure_role'),
    path('mentee-dashboard/', mentee_dashboard, name='mentee_dashboard'),
    path('mentor-dashboard/', mentor_dashboard, name='mentor_dashboard'),
]