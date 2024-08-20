from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from classperiod.models import Classperiod
from classes.models import Class
from course.models import Course



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields= "__all__"

class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields=["course_id","course_name","teacher"]




class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields = "__all__"

class MinimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.firstname} {object.lastname}"
    class Meta:
        model=Teacher
        fields = ["teacher_id","firstname","department"]


class ClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model= Classperiod
        fields= "__all__"

class MinimalClassperiodSerializer(serializers.ModelSerializer):
    courses=CourseSerializer(many=True)
    class Meta:
        model = Classperiod
        fields= ["start_time","end_time","courses"]
        


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model= Class
        fields= "__all__"

class MinimalClassSerializer(serializers.ModelSerializer):
    students= ClassSerializer(many=True)
    class Meta:
        model=Class
        fields= ["clas_id","class_name","class_duration","students"]



class StudentSerializer(serializers.ModelSerializer):
    courses= CourseSerializer(many=True)
    class Meta:
        model = Student
        fields= "__all__"

class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.firstname} {object.lastname}"
    class Meta:
        model=Student
        fields = ["id","firstname","email"]