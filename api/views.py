from django.shortcuts import render
from rest_framework import viewsets
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from event.models import AddEvent
from .serializers import *

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset=AddEvent.objects.all()
    serializer_class=EventSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
