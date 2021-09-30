from django.test import TestCase
from .models import Course
from django.urls import reverse


# Create your tests here.

class courseModelTestCase(TestCase):
    def setUp(self):
        self.course=Course(
            course_name="Love",
            trainer="AkiraChix",
            description="Hello. My name is Love Lace. I love Akirachix",
            course_code="bg0098",
            class_name="Bool",
         
            )
              

    def test_course_name(self):
        self.assert_(self.course.check_course_name())
    
    
    def test_course_trainer(self):
        self.assert_(self.course.check_trainer())

    def test_course_registration_view(self):
        url=reverse('course:register-course')
        data ={
            "course_name":self.course.course_name,
            "class_name":self.course.class_name,
            "description":self.course.description,
            "course_code":self.course.course_code,
            "trainer":self.course.trainer,
            }
   
        
        request=self.client.post(url,data,follow=True)
        self.assertEqual(request.status_code,200)
