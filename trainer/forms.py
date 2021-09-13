from django import forms
from django.db import models
from django.db.models import fields
from .models import Trainer


class RegisterTrainerForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields="__all__"
        widgets = {
            'first_name': forms.TextInput( attrs={'class': 'form-control','style':'width:88%','id':'fname'}),
            'last_name': forms.TextInput( attrs={'class': 'form-control','style':'width:88%',}),
            'age': forms.NumberInput(attrs={'class': 'form-control','style':'width:88%'}),            
            'nationality': forms.Select( attrs={'class': 'form-select','style':'width:88%'}),
            'national_id': forms.TextInput( attrs={'class': 'form-control','style':'width:88%'}),
            'email': forms.EmailInput( attrs={'class': 'form-control','style':'width:88%'}),
            'phone_number': forms.TextInput( attrs={'class': 'form-control','style':'width:88%'}),
            'image': forms.FileInput( attrs={'class': 'form-control','style':'width:88%'}),
            'resume': forms.ClearableFileInput( attrs={'class': 'form-control','style':'width:88%'}),
            'salary': forms.NumberInput( attrs={'class': 'form-control','style':'width:88%'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control','style':'width:88%'}),            
            'gender': forms.Select(attrs={'class': 'form-select','style':'width:88%'}), 
            'course_name': forms.TextInput( attrs={'class': 'form-control','style':'width:88%',}),
            'city': forms.TextInput( attrs={'class': 'form-control','style':'width:88%'}),
            'bio':forms.Textarea(attrs={'class': 'form-control','style':'width:88%'})
        }
        labels={
            'first_name':'First Name',
            'last_name': 'Last Name',
            'national_id':'National ID',
            'phone_number':'Phone Number',
            'course_name':'Course Name',
            'company_name':'Company Name',
           


        }

