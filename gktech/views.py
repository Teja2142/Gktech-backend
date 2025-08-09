from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    """
    API root endpoint providing links to all main endpoints.
    """
    return Response({
        'documentation': {
            'swagger': reverse('schema-swagger-ui', request=request, format=format),
            'redoc': reverse('schema-redoc', request=request, format=format),
        },
        'admin': '/admin/',
        'api_endpoints': {
            'users': '/api/v1/users/',
            'products': '/api/v1/products/',
            'careers': '/api/v1/careers/',
            'news': '/api/v1/news/',
            'contact': '/api/v1/contact/',
        }
    })

def home(request):
    """
    Home page view that renders the home.html template.
    """
    return render(request, 'home/index.html')
