from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from course.models import Assignment, Course

from core.models import ModificationTrackingModel


class Gender(models.TextChoices):
    FEMALE = "Female"
    MALE = "Male"
    PREFER_NOT_TO_SAY = "Prefer not to say"


class AssignmentStatus(models.TextChoices):
    PENDING = "Pending"
    DONE = "Done"
    SUBMITTED = "Submitted"


class Relationship(models.TextChoices):
    PARENT = "Parent"
    SIBLING = "Sibling"
    RELATIVE = "Relative"


class EmergencyContact(ModificationTrackingModel):
    full_name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        default="",
        help_text="Emergency contact's full name",
    )
    phone_number = PhoneNumberField(
        null=False,
        blank=False,
        help_text="emergency contact's phone number",
    )
    relationship = models.CharField(
        max_length=30,
        choices=Relationship.choices,
        null=False,
        blank=False,
        default=Relationship.PARENT,
        help_text="relationship to student",
    )


# Create your models here.
class Student(ModificationTrackingModel):
    first_name = models.CharField(
        max_length=30,
        null=False,
        help_text="First name of the student",
    )

    last_name = models.CharField(
        max_length=30,
        null=False,
        help_text="Last name of the student",
    )

    date_of_birth = models.DateField(
        blank=False,
        null=False,
        help_text="Student's date of birth in the format YYYY-MM-DD",
    )

    nationality = CountryField(
        null=False,
        blank=False,
        help_text="student's country of origin",
    )

    national_id = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        help_text="National ID number, if applicable",
    )

    email = models.EmailField(
        max_length=50,
        null=False,
        blank=False,
        help_text="Email address of the student",
    )

    phone_number = PhoneNumberField(
        max_length=30,
        null=True,
        blank=True,
        help_text="Phone number of the student, including country code",
    )

    profile_image = models.ImageField(
        upload_to="images/",
        null=True,
        help_text="Profile image of the student",
    )

    medical_report = models.FileField(
        upload_to="documents/",
        null=True,
        help_text="Medical report of the student, if available",
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        help_text="Date when the student joined",
    )

    gender = models.CharField(
        max_length=20,
        help_text="Gender of the student",
        choices=Gender.choices,
        default=Gender.PREFER_NOT_TO_SAY,
    )

    student_courses = models.ManyToManyField(
        Course,
        max_length=20,
        help_text="Class name the student is in",
        related_name="student_courses",
    )
    # TODO: make compulsory after data migration
    emergency_contact = models.ForeignKey(
        EmergencyContact,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Emergency contact for the student",
        related_name="emergency_contact",
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        return datetime.now().year - self.date_of_birth

    def __str__(self):
        return f"{self.full_name}"


class StudentAssignment(ModificationTrackingModel):
    student_name = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="student_name",
    )
    student_assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="student_assignments",
    )
    assignment_status = models.CharField(
        max_length=11,
        help_text="Assignemnt status",
        choices=AssignmentStatus.choices,
        default=AssignmentStatus.PENDING,
    )

    def __str__(self):
        return self.student_assignment.name
