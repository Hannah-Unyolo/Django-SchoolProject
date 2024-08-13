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
from rest_framework import status

class StudentListView(APIView):
    def get(self,request):
        students= Student.objects.all()
        firstname= request.query_params.get("firstname")
        if firstname:
            students= students.filter(firstname=firstname)

        country = request.query_params.get("country")
        if country:
            students= students.filter(country=country)
        serializer= StudentSerializer(students,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    def assign(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

class StudentDetailView(APIView):
    def get(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,id):
        student = Student.objects.get(id = id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def enroll(self,student,course_id):
        course = Course.objects.get(id=course_id)
        student.courses.add(course)
  

    def unenroll(self,student,course_id):
        course = Course.objects.get(id= course_id)
        student.courses.remove(course)
   

    def post(self,request,id):
        student=Student.objects.get(id=id)
        action = request.data.get("action")
        if action== "unenroll":
            course_id=request.data.get("course")
            self.unenroll(student,course_id)
        

        if action== "enroll":
            course_id = request.data.get("course")
            self.enroll(student,course_id)
        return Response(status.HTTP_202_ACCEPTED)
    
    def enrollclass(self,student,clas_id):
        classe = Class.objects.get(id=clas_id)
        student.classes.add(classe)

    def unenrollclass(self,student,clas_id):
        classe = Class.objects.get(id= clas_id)
        student.courses.remove(classe)

    def assign(self,request,id):
        student=Student.objects.get(id=id)
        action = request.data.get("action")
        if action== "unenrollclass":
            clas_id =request.data.get("class")
            self.unenrollclass(student,clas_id)
        

        if action== "enrollclass":
            clas_id = request.data.get("class")
            self.enrollclass(student,clas_id)
        return Response(status.HTTP_202_ACCEPTED)
    

class TeacherListView(APIView):
    def get(self,request):
        teachers= Teacher.objects.all()
        serializer = TeacherSerializer(teachers,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self,request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,id):
        teacher = Teacher.objects.get(id = id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    

class ClassperiodListView(APIView):
    def get(self,request):
        classperiods= Classperiod.objects.all()
        serializer= ClassperiodSerializer(classperiods,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ClassperiodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class ClassperiodDetailView(APIView):
    def get(self,request,id):
        classperiod = Classperiod.objects.get(id=id)
        serializer = ClassperiodSerializer(classperiod)
        return Response(serializer.data)
    
    def put(self,request,id):
        classperiod = Classperiod.objects.get(id=id)
        serializer = ClassperiodSerializer(classperiod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,id):
        classperiod = Classperiod.objects.get(id = id)
        classperiod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class ClassListView(APIView):
    def get(self,request):
        classes= Class.objects.all()
        serializer= ClassSerializer(classes,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class ClassDetailView(APIView):
    def get(self,request,id):
        classes = Class.objects.get(id = id)
        serializer = ClassSerializer(classes)
        return Response(serializer.data)
    
    def put(self,request,id):
        classes = Class.objects.get(id = id)
        serializer = ClassSerializer(classes,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,id):
        classes = Class.objects.get(id = id)
        classes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
        


class CourseListView(APIView):
    def get(self,request):
        courses= Course.objects.all()
        serializer= CourseSerializer(courses,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class CourseDetailView(APIView):
    def get(self,request,id):
        course = Course.objects.get(id = id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self,request,id):
        course = Course.objects.get(id = id)
        serializer = CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,id):
        course = Course.objects.get(id = id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
        


    





# Create your views here.
