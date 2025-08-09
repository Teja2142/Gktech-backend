from django.contrib import admin
from .models import JobPosting, JobApplication

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'location', 'is_active', 'created_at')
    list_filter = ('is_active', 'department', 'location', 'created_at')
    search_fields = ('title', 'description', 'requirements', 'responsibilities')
    ordering = ('-created_at',)
    list_editable = ('is_active',)
    
    fieldsets = (
        ('Job Information', {
            'fields': ('title', 'department', 'location', 'is_active')
        }),
        ('Job Details', {
            'fields': ('description', 'requirements', 'responsibilities'),
            'classes': ('wide',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job', 'status', 'created_at')
    list_filter = ('status', 'job', 'created_at')
    search_fields = ('name', 'email', 'phone', 'job__title')
    ordering = ('-created_at',)
    list_editable = ('status',)
    
    fieldsets = (
        ('Applicant Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Application Details', {
            'fields': ('job', 'resume', 'cover_letter', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at',)
