from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

# API Documentation schema
schema_view = get_schema_view(
    openapi.Info(
        title="GK Technologies API",
        default_version='v1',
        description="""
Welcome to the GK Technologies API documentation.

This API provides endpoints for managing:
* Products and Categories
* Career Opportunities and Job Applications
* News Articles
* User Management
* Contact Form Submissions

All endpoints support both form-data and JSON formats for POST/PUT requests.
File uploads (images, resumes) are handled through multipart/form-data.
        """,
        contact=openapi.Contact(email="contact@gktech.com"),
        license=openapi.License(name="BSD License"),
        tags=[
            {'name': 'Users', 'description': 'User management endpoints'},
            {'name': 'Products', 'description': 'Product and category management endpoints'},
            {'name': 'Careers', 'description': 'Job postings and applications endpoints'},
            {'name': 'News', 'description': 'News articles and categories endpoints'},
            {'name': 'Contact', 'description': 'Contact form submission endpoints'},
        ],
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# URL patterns
urlpatterns = [
    # Root endpoints
    path('', views.home, name='home'),
    # path('api/', views.api_root, name='api-root'),
    path('admin/', admin.site.urls),
    
    # API Documentation
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # API Endpoints
    path('api/v1/users/', include('users.urls')),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/careers/', include('careers.urls')),
    path('api/v1/news/', include('news.urls')),
    path('api/v1/contact/', include('contact.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
