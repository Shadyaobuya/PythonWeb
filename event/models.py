from django.db import models

# Create your models here.
class AddEvent(models.Model):
    event_name=models.CharField(max_length=30,null=True)
    venue=models.CharField(max_length=30,null=True)
    description=models.TextField(null=True)
    start_time=models.DateTimeField(null=True)
    end_time=models.DateTimeField(null=True)
    link=models.CharField(max_length=50,null=True)
    # attended=models.BooleanField(null=True)

    def __str__(self):
        return self.event_name

    def check_event_duration(self):

        return f'{self.end_time}'

    def check_event_venue(self):
        return f'{self.venue}'


    
    
