from django.urls import path
from . import views

app_name='event'
urlpatterns=[
    path("add-event/",views.add_event,name="add-event"),
    path("event-calendar/",views.CalendarView.as_view(),name="calendar"),
    path("event-list/",views.event_list,name="event-list"),
    path("edit-event/<int:id>/",views.edit_event,name="edit-event"),
    path("delete-event/<int:id>/",views.delete_event,name="delete-event"),



]