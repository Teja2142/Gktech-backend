from django.contrib import admin
from django.utils.html import format_html
from .models import NewsCategory, NewsArticle

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'image_preview', 'published_at')
    list_filter = ('category', 'is_featured', 'published_at')
    search_fields = ('title', 'content', 'category__name')
    ordering = ('-published_at',)
    list_editable = ('is_featured',)
    prepopulated_fields = {'slug': ('title',)}
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.image.url)
        return 'No Image'
    image_preview.short_description = 'Image Preview'
    
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'slug', 'category', 'is_featured')
        }),
        ('Content', {
            'fields': ('content', 'image'),
            'classes': ('wide',)
        }),
        ('Timestamps', {
            'fields': ('published_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('published_at', 'updated_at')
