from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractBaseUser):
#     pass


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    type = models.CharField(max_length=100, choices=[('Teacher', 'Teacher'), ('Student', 'Student')], default='Student')


class Teacher(models.Model):
    phone = models.CharField(max_length=20)
    time = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    salary = models.FloatField()


class Student(models.Model):
    dob = models.DateField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    alt_phone = models.CharField(max_length=20)

