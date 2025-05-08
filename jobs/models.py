from django.db import models

# Create your models here.
from django.db import models
from users.models import CustomUser

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    date_applied = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['job', 'applicant']