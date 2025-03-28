from django.urls import path
from .views import ConversationView, AddMessageView

urlpatterns = [
    path('message/list/', ConversationView.as_view(), name='conversation'),
    path('message/new/', AddMessageView.as_view(), name='add_message'),
]
