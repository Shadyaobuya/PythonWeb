from django.core.files.storage import default_storage
from django.db import models
import datetime
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=30,null=True)
    last_name=models.CharField(max_length=30,null=True)
    date_of_birth=models.DateField(blank=False,null=True)
    age=models.PositiveSmallIntegerField(null=True,default=20)
    NATIONALITY=(
        ('0','Kenyan'),
        ('1','Ugandan'),
        ('3','Rwandan'),
        ('4','South Sudanese')
    )
    nationality = models.CharField(max_length=11,choices=NATIONALITY,default="Kenyan")
    national_id=models.CharField(max_length=30,default=" ")
    email=models.EmailField(max_length=25, default="shadyaobuya@gmail.com")
    phone_number=PhoneNumberField(max_length=30,default=" ")
    image=models.ImageField( upload_to="images/",null=True)
    medical_report=models.FileField(upload_to="documents/",null=True)
    admission_date=models.DateField(null=True)
    academic_year=models.PositiveBigIntegerField(default=2021)
    CHOICES=(
        ('Female','Female'),
        ('Male','Male'),
        ('Other','Other'),

    )
    gender = models.CharField(max_length=11,choices=CHOICES,default="Female")
    laptop_number=models.CharField(max_length=10,null=True)
    class_name=models.CharField(max_length=20,default="Lovelace")
    guardian_name=models.CharField(max_length=20,default=" ")
    guardian_number=PhoneNumberField(max_length=30,default="+254729113940")

    def __str__(self):
        return self.first_name
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def year_of_birth(self):
        current_year=datetime.datetime.now().year
        return current_year-self.age
    
    
    


    
    
  

    
   

    
