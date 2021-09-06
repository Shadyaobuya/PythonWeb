from django import forms
from django.db import models
from django.db.models import fields
from .models import Student
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Student
        fields= "__all__"
        widgets = {
            'first_name': forms.TextInput( attrs={'class': 'form-control','style':'width:99%'}),
            'last_name': forms.TextInput( attrs={'class': 'form-control','style':'width:99%',}),
            'date_of_birth': DatePickerInput( attrs={'class': 'form-control','style':'width:88%'}),
            'age': forms.NumberInput(attrs={'class': 'form-control','style':'width:99%'}),            
            'nationality': forms.Select( attrs={'class': 'form-select','style':'width:99%'}),
            'national_id': forms.TextInput( attrs={'class': 'form-control','style':'width:99%'}),
            'email': forms.EmailInput( attrs={'class': 'form-control','style':'width:99%'}),
            'phone_number': forms.TextInput( attrs={'class': 'form-control','style':'width:99%'}),
            'image': forms.FileInput( attrs={'class': 'form-control','style':'width:99%'}),
            'medical_report': forms.ClearableFileInput( attrs={'class': 'form-control','style':'width:99%'}),
            'admission_date': DatePickerInput( attrs={'class': 'form-control','style':'width:88%'}),
            'academic_year': forms.NumberInput(attrs={'class': 'form-control','style':'width:99%'}),            
            'gender': forms.Select(attrs={'class': 'form-select','style':'width:99%'}), 
            'laptop_number':forms.TextInput( attrs={'class': 'form-control','style':'width:99%'}),
            'class_name':forms.TextInput( attrs={'class': 'form-control','style':'width:99%'}),
            'guardian_name': forms.TextInput( attrs={'class': 'form-control','style':'width:99%',}),
            'guardian_number': forms.TextInput( attrs={'class': 'form-control','style':'width:99%'}),
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
            'laptop_number':'Laptop Number',
            'class_name':'Class Name',
            'medical_report':'Medical Report',
            'admission_date':'Admission Date',
            'academic_year':'Academic Year',
            'guardian_name':"Guardian's Name",
            'guardian_number':"Guardian's Phone Number",


        }

			