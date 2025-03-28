from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "timestamp", "body_preview")  # Custom column for message preview
    search_fields = ("sender__username", "body")  # Allow searching by sender username and message body
    list_filter = ("timestamp",)  # Enable filtering by timestamp
    ordering = ("-timestamp",)  # Show newest messages first

    def body_preview(self, obj):
        """Show a preview of the message body in the admin list view."""
        return obj.body[:50] + "..." if len(obj.body) > 50 else obj.body
    body_preview.short_description = "Message Preview"
