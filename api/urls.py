from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import ClassListView
from .views import CourseListView
from .views import ClassperiodListView

urlpatterns=[
    path("students/", StudentListView.as_view(),name= 'student_list_view'),

]

urlpatterns=[
    path("teachers/", TeacherListView.as_view(),name= 'teacher_list_view'),
]


urlpatterns=[
    path("classes/", ClassListView.as_view(),name='class_list_view'),
]


urlpatterns=[
    path("classperiods/",ClassperiodListView.as_view(), name='classperiod_list_view'),
]


urlpatterns=[
    path("courses/", CourseListView.as_view(), name= 'course_list_view'),
]

