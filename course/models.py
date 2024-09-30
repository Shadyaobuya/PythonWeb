from django.db import models
from core.models import ModificationTrackingModel
from trainer.models import Trainer


class Course(ModificationTrackingModel):
    course_name = models.CharField(
        max_length=40,
        null=True,
        help_text="Enter the name of the course. Maximum 40 characters.",
    )

    course_code = models.CharField(
        max_length=20,
        null=True,
        help_text="Enter the course code. Maximum 20 characters.",
    )

    course_trainer = models.ForeignKey(
        Trainer,
        on_delete=models.PROTECT,
        related_name="trainer_courses",
        # null=False,
        # blank=False,
        null=True,
        help_text="Select the trainer responsible for the course.",
    )

    description = models.TextField(
        null=True,
        blank=True,
        help_text="Provide a brief description of the course.",
    )

    class Meta:
        db_table = "course"

    def __str__(self):
        return f"{self.course_name} - {self.course_trainer}"


class CourseSyllabus(ModificationTrackingModel):
    syllabus_course = models.OneToOneField(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        related_name="syllabus_courses",
        help_text="Select the course this syllabus belongs to.",
    )

    topic = models.TextField(
        null=True,
        help_text="Enter the topics covered in the syllabus.",
    )

    class Meta:
        db_table = "course_syllabus"

    def __str__(self):
        return f"{self.syllabus_course} - {self.topic}"


# TODO:Make course required
class Assignment(ModificationTrackingModel):
    name = models.CharField(
        max_length=30,
        default="",
        null=False,
        blank=False,
        help_text="Enter the name of the assignment. Maximum 30 characters.",
    )
    assignement_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        db_column="course",
        related_name="assignemnt_courses",
        # null=False,
        # blank=False,
        null=True,
        help_text="Course name tied to assignment",
    )

    document = models.FileField(
        upload_to="assignments",
        null=True,
        blank=True,
        help_text="Upload the assignment document. Allowed formats: PDF, DOCX.",
    )

    description = models.TextField(
        null=True,
        blank=True,
        help_text="Provide a brief description of the assignment.",
    )

    class Meta:
        db_table = "assignment_course"

    def __str__(self):
        return self.name
