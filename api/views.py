from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from classes.models import Class
from course.models import Course
from teacher.models import Teacher
from classperiod.models import Classperiod
from .serializers import TeacherSerializer
from .serializers import StudentSerializer
from .serializers import ClassperiodSerializer
from .serializers import ClassSerializer
from .serializers import CourseSerializer

class StudentListView(APIView):
    def get(self,request):
        students= Student.objects.all()
        serializer= StudentSerializer(students,many=True)
        return Response(serializer.data)
    

class TeacherListView(APIView):
    def get(self,request):
        teachers= Teacher.objects.all()
        serializer = TeacherSerializer(teachers,many=True)
        return Response(serializer.data)
    

class ClassperiodListView(APIView):
    def get(self,request):
        classperiods= Classperiod.objects.all()
        serializer= ClassperiodSerializer(classperiods,many=True)
        return Response(serializer.data)


class ClassListView(APIView):
    def get(self,request):
        classes= Class.objects.all()
        serializer= ClassSerializer(classes,many=True)
        return Response(serializer.data)

class CourseListView(APIView):
    def get(self,request):
        courses= Course.objects.all()
        serializer= CourseSerializer(courses,many=True)
        return Response(serializer.data)



# Create your views here.
