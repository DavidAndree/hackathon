from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Message
from .forms import MessageForm

class ConversationView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messaging/conversation.html"
    context_object_name = "messages"
    ordering = ['-timestamp']

class AddMessageView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = "messaging/add_message.html"
    success_url = reverse_lazy("messaging:conversation")  # Fix: Use namespace

    def form_valid(self, form):
        form.instance.sender = self.request.user  # Automatically set sender
        return super().form_valid(form)
