from django.db import models
from django.db.models.manager import BaseManager
from teacher.models import Teacher


class Course(models.Model):
    course_id = models.SmallIntegerField()
    course_name = models.CharField(max_length=20)
    course_description = models.TextField()
    department = models.CharField(max_length=20)
    course_instructor = models.CharField(max_length=20)
    assessment_requirements = models.TextField()
    course_fee = models.IntegerField()

    teacher= models.OneToOneField(Teacher, on_delete=models.CASCADE, null=True, blank=True)

    objects: BaseManager['Course']

# Create your models here.
