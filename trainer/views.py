from trainer.models import Trainer
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import RegisterTrainerForm

# Create your views here.

def register_trainer(request):
    if request.method=="POST":
        form=RegisterTrainerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register-trainer')
        else:
            print(form.errors)
    else:
        form=RegisterTrainerForm()
    return render(request,'trainer/register_trainer.html',{'form':form})
        
def trainer_list(request):
    trainers=Trainer.objects.all()
    return render(request,'trainer/trainer-list.html',{'trainers':trainers})

def edit_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    if request.method=="POST":
        form=RegisterTrainerForm(request.POST,instance=trainer)
        if form.is_valid():
            form.save()
            return redirect(reverse("trainer-list"), id=trainer.id)
        else:
            print(form.errors)
    else:
        form=RegisterTrainerForm(instance=trainer)
        return render(request,"trainer/edit_trainer.html",{'form':form})



def delete_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    trainer.delete()
    return redirect('trainer-list')

def trainer_profile(request,id):
    trainer=Trainer.objects.get(id=id)
    return render(request,'trainer/trainerprofile.html',{'trainer':trainer})



