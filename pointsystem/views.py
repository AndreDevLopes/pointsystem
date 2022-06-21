from django.http import JsonResponse
from django.contrib.auth import login
from rest_framework import status
from rest_framework.response import Response

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from secretaria.models import MacPermitido


def ping(request):
    data = {'ping': 'pong!'}
    return JsonResponse(data)


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            mac = MacPermitido.objects.get(mac=request.data['mac'])
            if mac.is_active:
                serializer = AuthTokenSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.validated_data['user']
                login(request, user)
                return super(LoginAPI, self).post(request, format=None)
            return Response({'mensage': 'mac não ativo'}, status=status.HTTP_401_UNAUTHORIZED)
        except MacPermitido.DoesNotExist:
            return Response({'mensage': 'mec não encontrado'}, status=status.HTTP_401_UNAUTHORIZED)
