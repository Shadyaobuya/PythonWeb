from django.db import models

# Create your models here.
class AddEvent(models.Model):
    event_name=models.CharField(max_length=30,null=True)
    venue=models.CharField(max_length=30,null=True)
    description=models.TextField(null=True)
    start_time=models.DateTimeField(null=True)
    end_time=models.DateTimeField(null=True)
    link=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.event_name


    
    
