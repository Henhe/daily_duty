from django.forms import ModelForm
from .models import CommandLine, SupportLine, Period, WorkHours, Employees, Dutyes


class CommandForm(ModelForm):
    class Meta:
        model = CommandLine
        fields = ('name',)


class LineForm(ModelForm):
    class Meta:
        model = SupportLine
        fields = ('name',)


class PeriodForm(ModelForm):
    class Meta:
        model = Period
        fields = ('month', 'year',)


class WorkHoursForm(ModelForm):
    class Meta:
        model = WorkHours
        fields = ('period', 'days_quantity',)


class EmployeeForm(ModelForm):
    class Meta:
        model = Employees
        fields = ('surname', 'name', 'middle_name', 'commandline', 'supportline',)


class DutyForm(ModelForm):
    class Meta:
        model = Dutyes
        fields = ('workhours', 'employee', 'commandline', 'supportline',)
