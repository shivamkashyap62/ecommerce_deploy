from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("title", "donor", "location", "created_at")
    search_fields = ("title", "location")