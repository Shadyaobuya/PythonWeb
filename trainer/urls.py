from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.register_trainer,name='register-trainer'),
    path('trainer-list/',views.trainer_list,name='trainer-list'),
    path('edit-trainer/<int:id>/',views.edit_trainer,name='edit-trainer'),
    path('delete-trainer/<int:id>/',views.delete_trainer,name='delete-trainer'),
    path('trainer-profile/<int:id>/',views.trainer_profile,name='trainer-profile'),


]