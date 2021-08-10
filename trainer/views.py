from django.shortcuts import redirect, render
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
        




