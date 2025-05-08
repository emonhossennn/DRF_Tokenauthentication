from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, ApplicationViewSet, PublicJobListView
from jobs.views import JobViewSet


router = DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('public/jobs/', PublicJobListView.as_view(), name='public-jobs'),
]
