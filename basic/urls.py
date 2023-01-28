from django.urls import path, include
from rest_framework import routers

from .views import SkillsViewSet, CourseViewSet, add_register_course, get_register_course

router = routers.DefaultRouter()

router.register('skills', SkillsViewSet)
router.register('course', CourseViewSet)
# router.register('register_course', RegistrationCourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register_course/', add_register_course),
    path('get_register_course/', get_register_course),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
