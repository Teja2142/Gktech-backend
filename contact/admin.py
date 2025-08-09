from django.contrib import admin
from django.utils import timezone
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'company', 'subject', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'company')
        }),
        ('Message', {
            'fields': ('subject', 'message', 'created_at')
        }),
        ('Response', {
            'fields': ('is_read', 'response', 'responded_at'),
        }),
    )
    
    def save_model(self, request, obj, form, change):
        # Update responded_at when a response is added
        if 'response' in form.changed_data and obj.response:
            obj.responded_at = timezone.now()
        super().save_model(request, obj, form, change)
