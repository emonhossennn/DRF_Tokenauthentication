from rest_framework import serializers
from .models import Job, Application

class JobSerializer(serializers.ModelSerializer):
    employer = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['created_date', 'employer']

class ApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['date_applied', 'applicant']

    def validate(self, data):
        if self.context['request'].user.role != 'job_seeker':
            raise serializers.ValidationError("Only job seekers can apply for jobs")
        return data
    
class ApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['date_applied', 'applicant']

    def validate(self, data):
        if self.context['request'].user.role != 'job_seeker':
            raise serializers.ValidationError("Only job seekers can apply for jobs")
        return data