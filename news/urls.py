from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsCategoryViewSet, NewsArticleViewSet

app_name = 'news'

router = DefaultRouter()
router.register('categories', NewsCategoryViewSet, basename='category')
router.register('', NewsArticleViewSet, basename='article')

urlpatterns = router.urls
