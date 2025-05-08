from django.shortcuts import render
from jobs.models import Job  # Correct import path
from users.models import Job  # Incorrect


# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserRegistrationSerializer

class RegisterView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'role': token.user.role
        })