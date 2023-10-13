import random
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from .serializers import *


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save(is_active=False)
    confirmation = UserConfirmation.objects.create(user=user, code=random.randint(100000, 999999))
    return Response({'status': 'User registered', 'code': confirmation.code, 'data': serializer.data},
                    status=HTTP_201_CREATED)


@api_view(['POST'])
def confirm_user_api_view(request):
    code = request.data.get('code', None)
    confirmation = get_object_or_404(UserConfirmation, code=code)
    user = confirmation.user
    user.is_active = True
    user.save()
    confirmation.delete()
    return Response({'status': 'User activated'}, status=HTTP_200_OK)


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    login(request, user)
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})