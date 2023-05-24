from django.contrib import admin


from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "is_talent", "is_client"]
    list_filter = ["date_joined"]


@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ["id", "talent_name", "user"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "user"]
