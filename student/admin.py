from django.contrib import admin
from .models import Student, StudentAssignment, EmergencyContact


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_filter = ("first_name", "last_name")
    list_display = ["full_name", "nationality", "gender"]
    search_fields = ("full_name",)


@admin.register(StudentAssignment)
class StudentAssignmentAdmin(admin.ModelAdmin):
    list_filter = ("student_name", "student_assignment", "assignment_status")
    list_display = ["student_name", "student_assignment", "assignment_status"]
    search_fields = ("student_name", "student_assignment", "assignment_status")


@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_filter = ("full_name", "phone_number", "relationship")
    list_display = ("full_name", "phone_number", "relationship")
    search_fields = ("full_name", "phone_number", "relationship")
