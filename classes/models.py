from django.db import models
from django.db.models.manager import BaseManager


class Class(models.Model):
    clas_id = models.SmallIntegerField()
    class_name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    enrollnment = models.SmallIntegerField()
    room_number = models.SmallIntegerField()
    class_duration = models.CharField(max_length=20)
    meeting_days = models.CharField(max_length=20)
    class_rep = models.CharField(max_length=20)
    class_capacity = models.SmallIntegerField()

    objects: BaseManager['Class']

# Create your models here.
