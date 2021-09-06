from django.urls import path
from . import views


urlpatterns=[
    path("add-event/",views.add_event,name="add-event"),
    path("event-calendar/",views.CalendarView.as_view(),name="calendar")
]