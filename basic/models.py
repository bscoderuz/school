from django.db import models
from django.core.validators import RegexValidator


# Create your models here.


class Skills(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/skills_pic')

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
    _validate_phone = RegexValidator(
        regex=r"^9\d{12}$",
        message="Telefon raqamingiz 9 bilan boshlanishi va 12 ta belgidan oshmasligi lozim. Masalan: 998993451545",
    )
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12, validators=[_validate_phone])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
