from rest_framework import serializers
from .models import Skills, Course, RegistrationCourse


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['name', 'image']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'time', 'duration', 'price', 'created', 'updated', 'skills']

    def to_representation(self, instance):
        to_rep = super().to_representation(instance)
        to_rep['skills'] = instance.name
        return to_rep


class RegistrationCourseSerializer(serializers.ModelSerializer):
    course = serializers.CharField(max_length=200)

    class Meta:
        model = RegistrationCourse
        fields = ['full_name', 'phone_number', 'course']

    def create(self, validated_data):
        name = validated_data.pop("course")
        try:
            course = Course.objects.get(name=name)
        except Course.DoesNotExist:
            raise serializers.ValidationError(f"Course with {name} name doesn't exist")
        validated_data["course"] = course
        return super().create(validated_data)

    def to_representation(self, instance):
        to_rep = super().to_representation(instance)
        to_rep['course'] = instance.course.name
        return to_rep
