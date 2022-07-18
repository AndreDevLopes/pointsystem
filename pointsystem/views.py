from django.http import JsonResponse
from django.contrib.auth import login
from datetime import date

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


def ping(request):
    data = {'ping': 'pong!'}
    return JsonResponse(data)


def DataHoje(request):
    data = {'hoje': date.today()}
    return JsonResponse(data)


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
