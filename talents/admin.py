from django.contrib import admin


from .models import *


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["education_school", "education_for"]
    list_filter = ["education_created"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["experience_title", "experience_for"]
    list_filter = ["experience_created"]


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ["certificate_name", "certificate_for"]
    list_filter = ["certificate_created"]
