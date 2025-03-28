from django.shortcuts import render
from django.views.generic import DetailView
from accounts.models import CustomUser


# Create your views here.
class UserListView(DetailView):
    model = CustomUser
    template_name = "user_detail.html"
