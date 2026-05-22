from django.contrib import admin
from .models import Request

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("receiver", "donation", "status")
    list_filter = ("status",)