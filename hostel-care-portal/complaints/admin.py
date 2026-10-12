from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Complaint

# Customizing the Admin/Warden portal header titles
AdminSite.site_header = "Hostel Care Portal - Warden Dashboard"
AdminSite.site_title = "Warden Portal"
AdminSite.index_title = "Manage Student Complaints"


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    # Columns displayed in the list view
    list_display = ("title", "user", "category", "status", "created_at")

    # Filters available on the right sidebar
    list_filter = ("status", "category", "created_at")

    # Search bar fields
    search_fields = ("title", "description", "user__username")

    # Order newest complaints first
    ordering = ("-created_at",)

    # Make created_at read-only
    readonly_fields = ("created_at",)