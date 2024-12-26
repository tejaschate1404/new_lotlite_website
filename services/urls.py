from django.urls import path
from services.views import details_Web_Development, services ,studentMobility ,student_mobility_course_detail ,update_course ,delete_course, view_course

from .views import  AddStudentMobilityView
from .views import view_student_mobility
urlpatterns = [
     path("services/",services),
     path("studentMobility/", studentMobility , name = 'student-mobility'),
     path("services/Web_Development",details_Web_Development),
     path("add_services/", AddStudentMobilityView.as_view(), name='add_services'),
     path('student-mobility-course/<int:course_id>/', student_mobility_course_detail, name='student_mobility_course_detail'),
     path('view-student-mobility', view_student_mobility, name='view_student_mobility'),
     path('student-mobility-courses/<int:course_id>/delete/', delete_course, name='delete_course_student_mobility'),
     path('student-mobility-courses/<int:course_id>/view/', view_course, name='view_course'),
     path('update_course/<int:course_id>/', update_course, name='update_course'),
     
]
