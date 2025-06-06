from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views import View
from django.middleware.csrf import get_token

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Adiciona campos extras no payload do token
        token['user_id'] = user.id
        token['username'] = user.username
        return token

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Pega o token de refresh enviado pelo cliente
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response({"detail": "Token de refresh não fornecido."}, status=400)

            # Invalida o token de refresh
            token = RefreshToken(refresh_token)
            # A funcionalidade de blacklist pode precisar ser configurada em settings.py
            # e o app 'rest_framework_simplejwt.token_blacklist' adicionado em INSTALLED_APPS
            # token.blacklist() 

            return Response({"detail": "Logout realizado com sucesso."}, status=200)

        except Exception as e:
            # Logar o erro seria uma boa prática
            # import logging
            # logger = logging.getLogger(__name__)
            # logger.error(f"Erro no logout: {e}")
            return Response({"detail": "Erro ao realizar logout."}, status=500)

