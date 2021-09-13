from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Trainer(models.Model):
    first_name=models.CharField(max_length=30,null=True)
    last_name=models.CharField(max_length=30,null=True)
    national_id=models.CharField(max_length=30,null=True)
    bio=models.TextField(null=True)
    email=models.EmailField(max_length=30,null=True)
    phone_number=PhoneNumberField(null=True)
    image=models.ImageField( upload_to="trainer_images/", null=True)
    resume=models.FileField(upload_to="trainer_documents/", null=True)
    salary=models.PositiveBigIntegerField(null=True)
    course_name=models.CharField(max_length=40,null=True)
    company_name=models.CharField(max_length=30,null=True)
    city=models.CharField(max_length=20,null=True)
    GENDER=(
        ('Female','Female'),
        ('Male','Male'),
        ('Other','Other'),
    )
    gender = models.CharField(max_length=11,choices=GENDER,null=True,default="other")

