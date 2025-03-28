from django.urls import path
from .views import SignupView, UserDetailView, UserListView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("users/", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>", UserDetailView.as_view(), name="user_detail"),
]
