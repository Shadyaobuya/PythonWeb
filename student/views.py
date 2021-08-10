from django.shortcuts import redirect, render
from .forms import StudentRegistrationForm


# Create your views here.

def register_student(request):
    if request.method=="POST":
        form=StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_student')
        else:
            print(form.errors)
    else:
        form=StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})


