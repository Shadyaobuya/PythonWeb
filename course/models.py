from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=40,null=True)
    course_code=models.CharField(max_length=20,null=True)
    trainer=models.CharField(max_length=10,null=True)
    description=models.TextField(null=True)
    class_name=models.CharField(max_length=20,null=True)

