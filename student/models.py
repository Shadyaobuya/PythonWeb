from django.db import models
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12,null=True)
    last_name=models.CharField(max_length=20,null=True)
    date_of_birth=models.DateField(blank=False,null=True)
    age=models.PositiveSmallIntegerField(null=True)
    NATIONALITY=(
        ('0','Kenyan'),
        ('1','Ugandan'),
        ('3','Rwandan'),
        ('4','South Sudanese')
    )
    nationality = models.CharField(max_length=11,choices=NATIONALITY,default="Kenyan")
    national_id=models.CharField(max_length=30,null=True)
    email=models.EmailField(max_length=25,null=True)
    phone_number=PhoneNumberField(max_length=30,null=True)
    image=models.ImageField( upload_to="images/", null=True)
    medical_report=models.FileField(upload_to="documents/",null=True)
    admission_date=models.DateField(null=True)
    academic_year=models.PositiveBigIntegerField(null=True)
    CHOICES=(
        ('Female','Female'),
        ('Male','Male'),
        ('Other','Other'),

    )
    gender = models.CharField(max_length=11,choices=CHOICES,null=True)
    laptop_number=models.CharField(max_length=10,null=True)
    class_name=models.CharField(max_length=20,null=True)
    guardian_name=models.CharField(max_length=20, null=True)
    guardian_number=PhoneNumberField(max_length=30,null=True)

    def __str__(self):
        return self.first_name
    
    
    


    
    
  

    
   

    
