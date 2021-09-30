from django.test import TestCase
from .models import AddEvent
from django.urls import reverse


# Create your tests here.

class eventModelTestCase(TestCase):
    def setUp(self):
        self.event=AddEvent(
            event_name="Love",
            venue="AkiraChix",
            description="Hello. My name is Love Lace. I love Akirachix",
            start_time="09/23/2021",
            end_time="09/23/2021",
            link="hsdufrefeijr/dslkfitrg/",
         
            )
              

    def test_event_duration(self):
        self.assert_(self.event.check_event_duration())
    
    
    def test_course_venue(self):
        self.assert_(self.event.check_event_venue())

    def test_event_registration_view(self):
        url=reverse('event:add-event')
        data ={
            "event_name":self.event.event_name,
            "venue":self.event.venue,
            "description":self.event.description,
            "start_time":self.event.start_time,
            "end_time":self.event.end_time,
            "link":self.event.link,
            }
   
        
        request=self.client.post(url,data,follow=True)
        self.assertEqual(request.status_code,200)
