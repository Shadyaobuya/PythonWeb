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
            return redirect('course:register-course')
        else:
            print(form.errors)
    else:
        form=CourseForm()
    return render(request,"course/register_course.html",{"form":form})

def courses_list(request):
    courses=Course.objects.all()
    return render (request,'course/course_list.html',{'courses':courses})

def course_syllabus(request,id):
    course=CourseSyllabus.objects.get(id=id)
    return render(request,'course/course-syllabus.html',{'course':course})

def edit_course(request,id):
    course=Course.objects.get(id=id)
    if request.method=='POST':
        form=CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect(reverse('course:course_list'), id=course.id)
        else:
            print(form.errors)
    else:
        form=CourseForm(instance=course)
        return render(request,"course/edit_course.html",{'form':form})

def delete_course(request,id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect(reverse('course:course_list'))