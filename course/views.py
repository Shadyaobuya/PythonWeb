from django import forms
from django.shortcuts import redirect, render
from .forms import CourseForm
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
