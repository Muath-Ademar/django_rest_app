from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        user = User.objects.get(username =request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user = user)
        response_data = {
            "token": token.key,
            "user": {
                "id": user.id,
                "username": user.username,
                "email" : user.email
                }
        }
        return Response(response_data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username = request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'detail': "not found."}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user = user)
    response_data = {
            "token": token.key,
            "user": {
                "id": user.id,
                "username": user.username,
                "email" : user.email
                }
        }
    return Response(response_data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def auth(request):
    return Response("this user is Authentecated")
