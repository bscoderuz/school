from rest_framework import generics
from .serializers import UserSerializer, RegisterSerializer
from .models import Users
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UsersView(generics.ListAPIView):
    queryset = Users.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
