from django.contrib import admin

from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "subscribed_at"]
    list_filter = ["subscribed_at"]
