from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        help_text='Your full name',
        style={'placeholder': 'John Doe'},
        required=True,
        error_messages={
            'required': 'Please provide your name'
        }
    )
    email = serializers.EmailField(
        help_text='Your email address for correspondence',
        style={'placeholder': 'john.doe@example.com'},
        required=True,
        error_messages={
            'required': 'Please provide your email address',
            'invalid': 'Please enter a valid email address'
        }
    )
    company = serializers.CharField(
        help_text='Your company or organization name',
        style={'placeholder': 'Acme Corporation'},
        required=False,
        allow_blank=True
    )
    subject = serializers.CharField(
        help_text='Brief subject of your inquiry',
        style={'placeholder': 'Product Inquiry'},
        required=True,
        error_messages={
            'required': 'Please provide a subject'
        }
    )
    message = serializers.CharField(
        help_text='Your detailed message or inquiry',
        style={
            'base_template': 'textarea.html',
            'placeholder': 'Please provide details about your inquiry...',
            'rows': 4
        },
        required=True,
        error_messages={
            'required': 'Please provide your message'
        }
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'company', 'subject', 'message']
