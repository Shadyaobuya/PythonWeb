from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from course.models import Course

# Create your views here.
def core_home(request):
    student=Student.objects.count()
    trainer=Trainer.objects.count()
    course=Course.objects.count()
    data={'students':student,'trainers':trainer,'courses':course}
    return render(request,'core/core_homepage.html',data)

def kk(request):
    return render (request,"core/kk.html")