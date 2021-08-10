from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12,null=True)
    last_name=models.CharField(max_length=20,null=True)
    date_of_birth=models.DateField(null=True)
    age=models.PositiveSmallIntegerField(null=True)
    NATIONALITY=(
        ('0','Kenyan'),
        ('1','Ugandan'),
        ('3','Rwandan'),
        ('4','South Sudanese')
    )
    nationality = models.CharField(max_length=11,choices=NATIONALITY,null=True,default="Kenyan")
    national_id=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=25,null=True)
    phone_number=PhoneNumberField(max_length=30,null=True)
    image=models.ImageField( upload_to="images/", null=True)
    medical_report=models.FileField(upload_to="documents/", null=True)
    admission_date=models.DateField(null=True)
    academic_year=models.PositiveBigIntegerField(null=True)
    CHOICES=(
        ('0','Female'),
        ('1','Male'),
        ('3','Other'),

    )
    
    gender = models.CharField(max_length=11,choices=CHOICES,null=True,default="other")
    guardian_name=models.CharField(max_length=20,null=True)
    guardian_number=PhoneNumberField(max_length=30,null=True)
    
    
    


    
    
  

    
   

    
