from django.db import models

# Create your models here.
class AddEvent(models.Model):
    event_name=models.CharField(max_length=30,null=True)
    date=models.DateField(null=True)
    venue=models.CharField(max_length=30,null=True)
    description=models.TextField(max_length=100,null=True)
    start_time=models.TimeField(null=True)
    end_time=models.TimeField(null=True)
    link=models.CharField(max_length=50,null=True)
    
    
