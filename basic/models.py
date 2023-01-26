from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Skills(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/skills_pic')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    skills = models.ManyToManyField(Skills, related_name='skills')

    def __str__(self):
        return self.name


class RegistrationCourse(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
