from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        help_text='Category name',
        style={'placeholder': 'Electronics'},
        required=True,
        error_messages={
            'required': 'Please provide a category name'
        }
    )
    description = serializers.CharField(
        help_text='Category description',
        style={
            'base_template': 'textarea.html',
            'placeholder': 'Electronic products and accessories',
            'rows': 3
        },
        required=True
    )

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        help_text='Product category ID',
        required=True,
        error_messages={
            'required': 'Please select a category',
            'does_not_exist': 'Invalid category selected'
        }
    )
    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )
    name = serializers.CharField(
        help_text='Product name',
        style={'placeholder': 'High-Performance LED Monitor'},
        required=True,
        error_messages={
            'required': 'Please provide a product name'
        }
    )
    description = serializers.CharField(
        help_text='Detailed product description',
        style={
            'base_template': 'textarea.html',
            'placeholder': 'A high-quality LED monitor with...',
            'rows': 4
        },
        required=True
    )
    features = serializers.JSONField(
        help_text='List of product features as JSON array',
        style={
            'base_template': 'textarea.html',
            'placeholder': '[\n  "4K Resolution",\n  "HDR Support",\n  "1ms Response Time"\n]',
            'rows': 5
        },
        required=True
    )
    specifications = serializers.JSONField(
        help_text='Product specifications as JSON object',
        style={
            'base_template': 'textarea.html',
            'placeholder': '{\n  "Screen Size": "27 inch",\n  "Resolution": "3840x2160",\n  "Refresh Rate": "144Hz"\n}',
            'rows': 6
        },
        required=True
    )
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Product price',
        style={'placeholder': '499.99'},
        required=True
    )
    image = serializers.ImageField(
        help_text='Product image file (JPEG/PNG, max 5MB)',
        style={'input_type': 'file'},
        required=True,
        error_messages={
            'required': 'Please upload a product image',
            'invalid': 'Please upload a valid image file'
        }
    )
    
    class Meta:
        model = Product
        fields = ['id', 'category', 'category_name', 'name', 'description', 'features', 'specifications', 'price', 'image', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
