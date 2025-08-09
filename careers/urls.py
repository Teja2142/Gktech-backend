from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobPostingViewSet, JobApplicationViewSet

app_name = 'careers'

router = DefaultRouter()
router.register('jobs', JobPostingViewSet, basename='job')
router.register('applications', JobApplicationViewSet, basename='application')

urlpatterns = router.urls
