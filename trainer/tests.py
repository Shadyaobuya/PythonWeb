from django.test import TestCase
from .models import Trainer
from django.urls import reverse


# Create your tests here.

class TrainerModelTestCase(TestCase):
    def setUp(self):
        self.trainer=Trainer(
            first_name="Love",
            last_name="AkiraChix",
            bio="Hello. My name is Love Lace. I love Akirachix",
            email="shadyaobuya@gmail.com",
            national_id="ajko667890",
            phone_number="+254729113940",
            course_name="Backend Web Development",
            salary=2021098877, 
            company_name="Sky Garden",
            city="Nairobi",
            gender="Male",
            resume="documents/Cover_Letter.pdf",  
            image="images/green.jpg" 
            )
              

    def test_full_name_contains_first_name(self):
        self.assertIn(self.trainer.first_name,self.trainer.full_name())
    
    def test_full_name_contains_last_name(self):
        self.assertIn(self.trainer.last_name,self.trainer.full_name())
    
    def test_course_taught(self):
        self.assert_(self.trainer.course_taught())

    def test_trainer_registration_view(self):
        url=reverse('trainer:register-trainer')
        data ={
            "first_name":self.trainer.first_name,
            "last_name":self.trainer.last_name,
            "bio":self.trainer.bio,
            "salary":self.trainer.salary,
            "company_name":self.trainer.company_name,
            "city":self.trainer.city,
            "gender":self.trainer.gender,
            "course_name":self.trainer.course_name,
            "email":self.trainer.email,
            "national_id":self.trainer.national_id,
            "phone_number":self.trainer.phone_number,
            "resume":self.trainer.resume,
            "image":self.trainer.image,

            }
   
        
        request=self.client.post(url,data,follow=True)
        self.assertEqual(request.status_code,200)
