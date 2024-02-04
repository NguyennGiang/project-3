from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from module.account.helper.srs import UserAuthSerializer, ObtainTokenSerializer
from services.authentication import JWTAuthentication

User = get_user_model()


# Create your views here.

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserAuthSerializer
    queryset = User.objects.all()


class LoginView(APIView):
    permission_classes = [AllowAny,]
    serializer_class = ObtainTokenSerializer

    def post(self, request):
        existed_user = User.objects.filter(email=request.data.get("email", "")).first()
        if not existed_user:
            return Response(data={"message": "Incorrect login information"}, status=400)
        if not existed_user.check_password(request.data.get("password", "")):
            return Response(data={"message": "Incorrect login information"}, status=400)
        jwt_token = JWTAuthentication.create_jwt(existed_user)
        return Response(data={**jwt_token, 'user': str(existed_user.id)}, status=200)


class LogoutView(APIView):
    pass
