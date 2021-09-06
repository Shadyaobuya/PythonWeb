from django.urls import path
from . import views

urlpatterns=[
    path('',views.core_home,name='home-page'),
     path('kk/',views.kk,name='kk'),

]
