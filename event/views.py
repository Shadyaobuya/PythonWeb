from django.shortcuts import render
from .forms import AddEventForm

# Create your views here.

def add_event(request):
    if request.method=="POST":
        form=AddEventForm()
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=AddEventForm()
    return render(request,'add-event.html',{'form':form})
    
    

