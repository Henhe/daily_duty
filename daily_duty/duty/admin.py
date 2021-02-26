from django.contrib import admin

# Register your models here.
from .models import Month
from .models import Period
from .models import WorkHours
from .models import Employees

admin.site.register(Month)
admin.site.register(Period)

class WhAdmin(admin.ModelAdmin) :
	list_display = ('period', 'days_quantity', 'workhours_sum')
	search_fields = ('period',)

admin.site.register(WorkHours, WhAdmin)

class EmployeesAdmin(admin.ModelAdmin) :
	list_display = ('full_name', 'surname', 'name', 'middle_name')
	search_fields = ('surname',)

admin.site.register(Employees, EmployeesAdmin)
