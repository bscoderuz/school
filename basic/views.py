from rest_framework import serializers, viewsets, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SkillsSerializer, CourseSerializer, RegistrationCourseSerializer
from .models import Skills, Course, RegistrationCourse

# Create your views here.

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_register_course(self):
    snippets = RegistrationCourse.objects.all()
    serializer = RegistrationCourseSerializer(snippets, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# def add_register_course(request):
#     serializer = RegistrationCourseSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterCourseViewSet(generics.ListCreateAPIView):
    queryset = RegistrationCourse.objects.all()
    serializer_class = RegistrationCourseSerializer
