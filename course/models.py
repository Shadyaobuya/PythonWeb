from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=40,null=True)
    course_code=models.CharField(max_length=20,null=True)
    trainer=models.CharField(max_length=30,null=True)
    description=models.TextField(null=True)
    class_name=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.course_name

# class Topic(models.Model):
#     topic_name=models.TextField(max_length=30,null=True)
#     description=models.CharField(max_length=30,null=True)
#     duration=models.PositiveSmallIntegerField(null=True)

#     def __str__(self):
#         return self.topic_name


class CourseSyllabus(models.Model):
    course=models.OneToOneField(Course,on_delete=SET_NULL,null=True)
    topic=models.TextField(null=True)
    
    def __str__(self):
        return self.topic




       








