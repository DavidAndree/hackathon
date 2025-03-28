from django.urls import path
from .views import SignupView, TestView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
]
