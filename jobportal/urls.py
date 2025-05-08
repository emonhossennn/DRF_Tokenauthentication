from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import RegisterView, CustomAuthToken
from jobs.views import JobViewSet, PublicJobListView, ApplicationCreateView

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view()),
    path('api/login/', CustomAuthToken.as_view()),
    path('api/jobs/public/', PublicJobListView.as_view()),
    path('api/applications/', ApplicationCreateView.as_view()),
    path('api/', include(router.urls)),
]