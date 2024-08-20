from django.db import models
from django.db.models.manager import BaseManager

# from course.models import Course
from classes.models import Class

class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    code = models.PositiveBigIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    bio = models.TextField()
    # courses = models.ManyToManyField(Course)
    classe = models.ManyToManyField(Class)

    objects: BaseManager['Student']

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

# Create your models here.
