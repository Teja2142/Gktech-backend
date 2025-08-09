from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

app_name = 'contact'

router = DefaultRouter()
router.register('', ContactViewSet, basename='contact')

urlpatterns = router.urls
