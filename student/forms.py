from django import forms
from django.db import models
from django.db.models import fields
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Student
        fields= "__all__"
        widgets = {
            'first_name': forms.TextInput( attrs={'class': 'form-control','style':'width:88%','id':'fname'}),
            'last_name': forms.TextInput( attrs={'class': 'form-control','style':'width:88%',}),
            'date_of_birth': forms.DateInput( attrs={'class': 'form-control','style':'width:88%'}),
            'age': forms.NumberInput(attrs={'class': 'form-control','style':'width:88%'}),            
            'nationality': forms.Select( attrs={'class': 'form-select','style':'width:88%'}),
            'national_id': forms.TextInput( attrs={'class': 'form-control','style':'width:88%'}),
            'email': forms.EmailInput( attrs={'class': 'form-control','style':'width:88%'}),
            'phone_number': forms.TextInput( attrs={'class': 'form-control','style':'width:88%'}),
            'image': forms.FileInput( attrs={'class': 'form-control','style':'width:88%'}),
            'medical_report': forms.ClearableFileInput( attrs={'class': 'form-control','style':'width:88%'}),
            'admission_date': forms.DateInput( attrs={'class': 'form-control','style':'width:88%'}),
            'academic_year': forms.NumberInput(attrs={'class': 'form-control','style':'width:88%'}),            
            'gender': forms.Select(attrs={'class': 'form-select','style':'width:88%'}), 
            'guardian_name': forms.TextInput( attrs={'class': 'form-control','style':'width:88%',}),
            'guardian_number': forms.TextInput( attrs={'class': 'form-control','style':'width:88%'}),
        }
        labels={
            'first_name':'First Name',
            'last_name': 'Last Name',
            'date_of_birth':'Date Of Birth',
            'age':'Age',
            'nationality':'Nationality',
            'national_id':'National ID',
            'email':'Email',
            'phone_number':'Phone Number',
           
            'medical_report':'Medical Report',
            'admission_date':'Admission Date',
            'academic_year':'Academic Year',
            'guardian_name':"Guardian's Name",
            'guardian_number':"Guardian's Phone Number",


        }

			