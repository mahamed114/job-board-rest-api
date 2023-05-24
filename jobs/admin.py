from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["id", "job_title", "posted_by"]
    list_filter = ["created_at"]
