from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from django.core.mail import send_mail
from django.conf import settings

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint for handling contact form submissions.
    Only POST method is allowed for submitting contact forms.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to submit contact form
    http_method_names = ['post']  # Only allow POST requests
    swagger_tags = ['Contact']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()
        
        # Send email notification to admin
        subject = f'New Contact Form Submission: {contact.subject}'
        message = f"""
        New contact form submission from {contact.name}
        
        Email: {contact.email}
        Company: {contact.company}
        Subject: {contact.subject}
        Message: {contact.message}
        """
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Failed to send email notification: {e}")

        return Response(serializer.data, status=status.HTTP_201_CREATED)
