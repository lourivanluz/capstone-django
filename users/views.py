from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from django.contrib.auth import authenticate

from users.serializers import UsersSerializer, LoginSerializer
from users.models import Users


class UserView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = []
    queryset = Users.objects
    serializer_class = UsersSerializer

    def get(self, request: Request, *args, **kwargs):
        if request.GET.get("username"):
            self.queryset = Users.objects.filter(
                username=request.GET.get("username")
            ).all()
            return super().get(request, *args, **kwargs)
        if request.GET.get("email"):
            self.queryset = Users.objects.filter(email=request.GET.get("email")).all()
            return super().get(request, *args, **kwargs)

        return super().get(request, *args, **kwargs)


@api_view(["POST"])
def loguin(request: Request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(True)

    user: Users = authenticate(**serializer.validated_data)
    if not user:
        return Response({"details": "invalide credentials"}, HTTP_400_BAD_REQUEST)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key}, HTTP_200_OK)
