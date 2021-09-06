from django import forms
from django.db.models import fields
from django.db import models
from django.forms.widgets import DateInput
from .models import AddEvent
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput



class AddEventForm(forms.ModelForm):
    class Meta:
        model=AddEvent
        fields="__all__"
        widgets={
            "event_name":forms.TextInput( attrs={'class': 'form-control','style':'width:99%','placeholder':'Event Name','id':'forminput'}),
            "venue":forms.TextInput( attrs={'class': 'form-control','style':'width:99%','placeholder':'Venue','id':'forminput'}),
            "start_time":forms.DateTimeInput(attrs={'class': 'form-control','placeholder':'Start Time','id':'forminput','type': 'datetime-local'}),
            "end_time":forms.DateTimeInput(attrs={'class': 'form-control','placeholder':'End Time','id':'forminput','type': 'datetime-local'}),
            "description":forms.Textarea( attrs={'class': 'form-control','style':'width:99%','placeholder':'Description','id':'forminput'}),
            "link":forms.TextInput( attrs={'class': 'form-control','style':'width:99%','placeholder':'Link','id':'forminput'}),
        }
        labels={
            "event_name":"Name",
            "start_time":"Start Time",
            "end_time":"End Time",
        }