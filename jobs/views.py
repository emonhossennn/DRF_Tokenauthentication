from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer
from .permissions import IsEmployer, IsJobOwner

class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [IsEmployer & IsJobOwner]
    
    def get_queryset(self):
        return Job.objects.filter(employer=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)

from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

class PublicJobListView(ListAPIView):
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location', 'job_type']
    
    def get_queryset(self):
        queryset = Job.objects.filter(is_active=True)
        
        # Search functionality
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return queryset
    

    from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

class PublicJobListView(ListAPIView):
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location', 'job_type']
    
    def get_queryset(self):
        queryset = Job.objects.filter(is_active=True)
        
        # Search functionality
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return queryset