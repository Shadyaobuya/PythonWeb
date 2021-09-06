from django import forms
from django.shortcuts import redirect, render
from .forms import CourseForm
from django.urls import reverse
from .models import *
# Create your views here.

def register_course(request):
    if request.method=="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register-course')
        else:
            print(form.errors)
    else:
        form=CourseForm()
    return render(request,"course/register_course.html",{"form":form})

def courses_list(request):
    courses=Course.objects.all()
    return render (request,'course/course_list.html',{'courses':courses})



def course_syllabus(request,pk):
    prk=CourseSyllabus.objects.get(id=pk)
    context={'prk':prk}
    return render(request,'course/course-syllabus.html',context)

def edit_course(request,id):
    course=Course.objects.get(id=id)
    if request.method=='POST':
        form=CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect(reverse('edit-course'),id=course.id)
        else:
            print(form.errors)
    else:
        form=CourseForm()
        return render(request,"course/edit_course.html",{'form':form})
        
