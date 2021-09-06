from calendar import calendar
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import AddEventForm
from .models import *
from .utils import Calendar
from django.views.generic.list import ListView
from datetime import date, datetime,timedelta
from django.utils.safestring import mark_safe
import calendar
# Create your views here.

def add_event(request):
    if request.method=="POST":
        form=AddEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
        else:
            print(form.errors)
    else:
        form=AddEventForm()
    return render(request,'event/add-event.html',{'form':form})




class CalendarView(ListView):
    model =AddEvent
    template_name = 'event/event-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('month', None))

        cal = Calendar(d.year, d.month, )

        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context



def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
