from rest_framework import viewsets, permissions
from .models import NewsCategory, NewsArticle
from .serializers import NewsCategorySerializer, NewsArticleSerializer

class NewsCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing news categories.
    """
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    swagger_tags = ['News']

class NewsArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing news articles.
    """
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    swagger_tags = ['News']
    filterset_fields = ['category', 'is_featured']
    search_fields = ['title', 'content']
    ordering_fields = ['published_at', 'title']
    lookup_field = 'slug'
