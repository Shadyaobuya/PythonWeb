from django.test import TestCase
from .models import Student
from django.urls import reverse
import datetime


# Create your tests here.

class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(
            first_name="Love",
            last_name="AkiraChix",
            age=19,
            nationality="0",
            date_of_birth="09/23/2021",
            email="shadyaobuya@gmail.com",
            national_id="ajko667890",
            phone_number="+254729113940",
            guardian_number="+254729113940",
            guardian_name="Mary Wanjiku",
            academic_year=2021, 
            admission_date="09/23/2021",
            laptop_number=171,
            medical_report="documents/Cover_Letter.pdf",  
            image="images/green.jpg" 
            )

    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())
    
    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())
    
    def test_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.student.age
        self.assertEqual(year,self.student.year_of_birth())

    def test_student_registration_view(self):
        url=reverse('student:register_student')
        data ={"first_name":self.student.first_name,
               "last_name":self.student.last_name,
               "age":self.student.age,
                "gender":self.student.gender,
               "class_name":self.student.class_name,
               "nationality":self.student.nationality,
                "laptop_number":self.student.laptop_number,
                "date_of_birth":self.student.date_of_birth,
               "email":self.student.email,
               "national_id":self.student.national_id,
               "phone_number":self.student.phone_number,
               "medical_report":self.student.medical_report,
               "laptop_number":self.student.laptop_number,
               "guardian_number":self.student.guardian_number,
               "guardian_name":self.student.guardian_name,
                "academic_year":self.student.academic_year,
                "admission_date":self.student.admission_date,
                "image":self.student.image,

            }
   
        
        request=self.client.post(url,data,follow=True)
        self.assertEqual(request.status_code,200)
