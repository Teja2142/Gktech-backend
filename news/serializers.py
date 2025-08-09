from rest_framework import serializers
from .models import NewsCategory, NewsArticle

class NewsCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        help_text='News category name',
        style={'placeholder': 'Technology'},
        required=True,
        error_messages={
            'required': 'Please provide a category name'
        }
    )
    description = serializers.CharField(
        help_text='Category description',
        style={
            'base_template': 'textarea.html',
            'placeholder': 'News about technology and innovation',
            'rows': 3
        },
        required=True
    )

    class Meta:
        model = NewsCategory
        fields = ['id', 'name', 'description']

class NewsArticleSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=NewsCategory.objects.all(),
        help_text='News category ID',
        required=True
    )
    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )
    
    class Meta:
        model = NewsArticle
        fields = ['id', 'title', 'slug', 'category', 'category_name', 'content', 
                 'summary', 'image', 'published_at', 'updated_at', 'is_featured']
        read_only_fields = ['slug', 'published_at', 'updated_at']
        extra_kwargs = {
            'title': {
                'help_text': 'Article title',
                'style': {'placeholder': 'New Technology Breakthrough'}
            },
            'content': {
                'help_text': 'Article content in markdown format',
                'style': {'base_template': 'textarea.html', 'rows': 10}
            },
            'summary': {
                'help_text': 'Brief article summary',
                'style': {'base_template': 'textarea.html', 'rows': 3}
            },
            'image': {
                'help_text': 'Article featured image (JPEG/PNG, max 5MB)',
                'style': {'input_type': 'file'}
            }
        }
