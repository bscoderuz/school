from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Users
from .serializers import RegisterSerializer
from rest_framework import generics


# Create your views here.


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer