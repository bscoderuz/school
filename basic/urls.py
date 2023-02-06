from django.urls import path, include
from rest_framework import routers

from .views import SkillsViewSet, CourseViewSet, RegisterCourseViewSet, get_register_course

router = routers.DefaultRouter()

app_name = 'basic'

router.register('skills', SkillsViewSet)
router.register('course', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_register_course/', get_register_course),
    path('register_course/', RegisterCourseViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
