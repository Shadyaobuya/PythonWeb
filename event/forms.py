from django import forms
from django.db.models import fields
from django.db import models
from .models import AddEvent


class AddEventForm(forms.ModelForm):
    class Meta:
        model=AddEvent
        fields="__all__"