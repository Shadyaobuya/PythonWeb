from django.urls import path,include
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register("students",StudentViewSet)
router.register("trainers",TrainerViewSet)
router.register("courses",CourseViewSet)
router.register("events",EventViewSet)

urlpatterns=[
    path("",include(router.urls))
]
