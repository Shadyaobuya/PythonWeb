from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.register_course,name="register-course"),
    path('course_list/',views.courses_list,name='course_list'),
    path('syllabus/<int:pk>/', views.course_syllabus,name='course-syllabus'),
    path('edit-course/<int:id>/', views.edit_course,name='edit-course'),


]