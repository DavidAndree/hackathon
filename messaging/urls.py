from django.urls import path
from .views import ConversationView, AddMessageView

app_name = 'messaging'  # Namespacing the app

urlpatterns = [
    path('', ConversationView.as_view(), name='conversation'),  # Access via /message/
    path('new/', AddMessageView.as_view(), name='add_message'),  # Access via /message/new/
]
