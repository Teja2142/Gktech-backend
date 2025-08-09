from rest_framework import serializers
from .models import JobPosting, JobApplication

class JobPostingSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        help_text='Job position title',
        style={'placeholder': 'Senior Software Engineer'},
        required=True
    )
    description = serializers.CharField(
        help_text='Detailed job description including responsibilities and requirements',
        style={
            'base_template': 'textarea.html',
            'placeholder': 'We are looking for an experienced software engineer...'
        },
        required=True
    )
    requirements = serializers.CharField(
        help_text='List of job requirements and qualifications',
        style={
            'base_template': 'textarea.html',
            'placeholder': '- 5+ years of experience\n- Bachelor\'s degree in Computer Science\n- Strong Python skills'
        },
        required=True
    )
    location = serializers.CharField(
        help_text='Job location (city, country or remote)',
        style={'placeholder': 'New York, USA or Remote'},
        required=True
    )
    
    class Meta:
        model = JobPosting
        fields = ('id', 'title', 'description', 'requirements', 'location', 'created_at', 'is_active')
        read_only_fields = ('created_at',)

class JobApplicationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        help_text='Your full name',
        style={'placeholder': 'John Doe'},
        required=True
    )
    email = serializers.EmailField(
        help_text='Your email address',
        style={'placeholder': 'john.doe@example.com'},
        required=True
    )
    phone = serializers.CharField(
        help_text='Your contact number',
        style={'placeholder': '+1 (555) 123-4567'},
        required=True
    )
    cover_letter = serializers.CharField(
        help_text='Introduce yourself and explain why you would be a good fit for this position',
        style={
            'base_template': 'textarea.html',
            'placeholder': 'Dear Hiring Manager,...'
        },
        required=True
    )
    resume = serializers.FileField(
        help_text='Upload your resume (PDF format preferred, max size 5MB)',
        style={'input_type': 'file'},
        required=True
    )
    job = serializers.PrimaryKeyRelatedField(
        queryset=JobPosting.objects.all(),
        help_text='The job position you are applying for',
        required=True
    )
    
    class Meta:
        model = JobApplication
        fields = ('name', 'email', 'phone', 'cover_letter', 'resume', 'job')
        read_only_fields = ('status',)
