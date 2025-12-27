# resume/admin.py

from django.contrib import admin
from .models import Resume

# This decorator registers the model with custom settings
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    """
    Customize how Resume appears in the admin panel
    """
    
    # Columns to show in the list view
    list_display = ('full_name', 'user', 'contact_email', 'updated_at')
    
    # Fields to search by
    search_fields = ('full_name', 'user__username', 'contact_email')
    
    # Filter options on the right side
    list_filter = ('created_at', 'updated_at')
    
    # Make these fields read-only (can't edit)
    readonly_fields = ('created_at', 'updated_at')
    
    # Organize fields into sections
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'full_name')
        }),
        ('About', {
            'fields': ('about_me',)
        }),
        ('Professional Details', {
            'fields': ('skills', 'education', 'projects', 'experience')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone', 'contact_address')
        }),
        ('Social Links', {
            'fields': ('linkedin', 'github')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Makes this section collapsible
        }),
    )