from student.models import Student
from django.shortcuts import redirect, render
from .forms import StudentRegistrationForm
from django.urls import reverse
from course.models import Course,CourseSyllabus
from django.views.generic.list import ListView
from django.db.models import Q

from django.core.paginator import Paginator



# Create your views here.

def register_student(request):
    if request.method=="POST":
        form=StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student:register_student')
        else:
            print(form.errors)
    else:
        form=StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})

def student_list(request):
    student_list=Student.objects.all()
    paginator = Paginator(student_list, 8) 

    page = request.GET.get('page')
    students = paginator.get_page(page)

    return render (request,'student_list.html',{'students':students})











def student_courses(request):
    courses=Course.objects.all()
    return render (request,'student_courses.html',{'courses':courses})

def home(request):
    return render (request,"home.html")

def view_profile(request,id):
    primary_key=Student.objects.get(id=id)
    context={'id':primary_key}
    return render(request,"student_profile.html",context)

def edit_student(request, id):
    student= Student.objects.get(id=id)
    if request.method == "POST":
        form=StudentRegistrationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student:student-profile", id=student.id)
    else:
        form= StudentRegistrationForm(instance=student)
        return render(request,"edit_profile.html", {"form":form})
        

def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('student:student-list')


def search_student(request):
    search_post = request.GET.get('search')
    if search_post:
        students = Student.objects.filter(Q(first_name__icontains=search_post))
        results=students.count()
    else:
        students = Student.objects.all()
        message="Looks like the student doesn't exist. Try searching using the first name"
        return render (request,'student_list.html',{'students':students,'message':message})

    return render (request,'student_list.html',{'students':students,'results':results})

