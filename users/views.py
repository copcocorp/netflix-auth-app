#from django.shortcuts import render

# Create your views here.

# users/views.py
"""from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({'error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'Usuario creado con éxito'}, status=status.HTTP_201_CREATED)
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def register(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    
    if not username or not password or not email:
        return Response({'error': 'Username, password and email are required'}, 
                      status=status.HTTP_400_BAD_REQUEST)
    
    if CustomUser.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, 
                      status=status.HTTP_400_BAD_REQUEST)
    
    user = CustomUser.objects.create_user(
        username=username,
        password=password,
        email=email
    )
    
    return Response({'message': 'User registered successfully'}, 
                  status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, 
                      status=status.HTTP_401_UNAUTHORIZED)