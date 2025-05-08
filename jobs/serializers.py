from rest_framework import serializers
from .models import Job, Application

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['employer', 'created_date']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['applicant', 'date_applied']

    def validate(self, data):
        user = self.context['request'].user
        if not hasattr(user, 'profile') or user.profile.role != 'job_seeker':
            raise serializers.ValidationError("Only job seekers can apply.")
        return data

    def create(self, validated_data):
        validated_data['applicant'] = self.context['request'].user
        return super().create(validated_data)
