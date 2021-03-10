from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from duty.models import Month
from duty.models import Period
from duty.models import WorkHours

def index(request):
	# s = ''
	# for month in Month.objects.filter(name_int__gte = 5):
	# 	s += month.name + str(month.name_int) + '\n'
	month = Month.objects.get(pk = 1)
	period = Period.objects.get(month = month, year = 2021)
	wh = WorkHours.objects.get(period = period)
	return HttpResponse(str(wh))