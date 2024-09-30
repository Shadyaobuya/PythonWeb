from django.urls import path
from . import views

app_name = "core"
# urlpatterns = []
urlpatterns = [
    path("", views.core_home, name="home-page"),
    # path("kk/", views.kk, name="kk"),
    #  path('login/google/',views.EmailBackend, name='login-google')
]
