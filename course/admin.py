from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.Course)
# admin.site.register(models.CourseSyllabus)
# admin.site.register(models.Assignment)
# admin.site.register(Topic)


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = ("course_name", "course_code", "course_trainer")
    list_display = ("course_name", "course_code", "course_trainer")
    search_fields = ("course_name", "course_code", "course_trainer")


@admin.register(models.CourseSyllabus)
class CourseSyllabusAdmin(admin.ModelAdmin):
    list_filter = ("syllabus_course", "topic")
    list_display = ("syllabus_course", "topic")
    search_fields = ("syllabus_course", "topic")


@admin.register(models.Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_filter = ("name", "description")
    list_display = ("name", "description")
    search_fields = ("name", "assignment_course__name", "description")
