from rest_framework import viewsets, permissions, filters
from .models import JobPosting, JobApplication
from .serializers import JobPostingSerializer, JobApplicationSerializer

class JobPostingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Job Postings.
    
    list: Return a list of all active job postings.
    create: Create a new job posting (admin only).
    retrieve: Return the details of a specific job posting.
    update: Update a job posting (admin only).
    delete: Delete a job posting (admin only).
    """
    swagger_tags = ['Careers']
    queryset = JobPosting.objects.filter(is_active=True)
    serializer_class = JobPostingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'department', 'location']
    ordering_fields = ['created_at', 'title']

class JobApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Job Applications.
    
    list: Return a list of all job applications (admin only).
    create: Submit a new job application (public access).
    retrieve: Return the details of a specific job application (admin only).
    update: Update a job application status (admin only).
    delete: Delete a job application (admin only).
    """
    swagger_tags = ['Careers']
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    
    def get_permissions(self):
        """
        Allow public access for job application submissions,
        but require authentication for other operations.
        """
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
    def get_queryset(self):
        """
        Return all applications for staff users,
        no access for non-staff users.
        """
        if self.request.user.is_staff:
            return JobApplication.objects.all()
        return JobApplication.objects.none()
