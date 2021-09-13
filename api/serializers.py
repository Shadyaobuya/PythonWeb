from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from event.models import AddEvent

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('first_name','last_name','age')

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=('first_name','last_name','bio')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddEvent
        fields=('event_name','venue','description')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=('course_name','trainer','description')