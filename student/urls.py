from django.urls import path
from .views import (
    home,
)

app_name = "student"
urlpatterns = [
    # path("register/", register_student, name="register_student"),
    path("student-home/", home, name="student-home"),
    #     path("list/", student_list, name="student-list"),
    #     path("my-courses/", student_courses, name="student-courses"),
    #     path("student-profile/<int:id>/", view_profile, name="student-profile"),
    #     path("edit-profile/<int:id>/", edit_student, name="edit-profile"),
    #     path("delete-profile/<int:id>/", delete_student, name="delete-profile"),
    #     path("search-student/", search_student, name="search-student"),
]
