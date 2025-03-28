from django.contrib import admin
from .models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("start_date", "end_date", "status")  # Display columns in admin
    list_filter = ("status",)  # Add filtering by status
    search_fields = ("start_date", "end_date")  # Allow searching by dates
