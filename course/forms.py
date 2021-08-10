from django import forms
from django.db import models
from django.forms import fields
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"
        widgets={
            "course_name":forms.TextInput( attrs={'class': 'form-control','style':'width:80%'}),
            "course_code":forms.TextInput( attrs={'class': 'form-control','style':'width:80%'}),
            "trainer":forms.TextInput( attrs={'class': 'form-control','style':'width:80%'}),
            "class_name":forms.TextInput( attrs={'class': 'form-control','style':'width:80%'}),
            "description":forms.Textarea( attrs={'class': 'form-control','style':'width:80%'}),
        }
        labels={
            "course_name":"Course Name",
            "course_code":"Course Code",
            "class_name":"Class Name",
        }
        
       