from rest_framework import viewsets, permissions, generics, filters, serializers
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


# Only employers can manage their own jobs
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'employer':
            return Job.objects.filter(employer=user)
        return Job.objects.none()

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)


# Public job listing with filters
class PublicJobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'location', 'job_type']


# Job seeker applies to a job
class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        job = serializer.validated_data['job']
        user = self.request.user

        if user.role != 'job_seeker':
            raise serializers.ValidationError("Only job seekers can apply.")

        if Application.objects.filter(job=job, applicant=user).exists():
            raise serializers.ValidationError("You have already applied to this job.")

        serializer.save(applicant=user)
