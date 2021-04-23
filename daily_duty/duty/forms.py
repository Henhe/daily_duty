from django.forms import ModelForm, CharField, PasswordInput, ValidationError
from .models import CommandLine, SupportLine, Period, WorkHours, Employees, Dutyes
from django.contrib.auth.models import User

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

class DutyFormReport(ModelForm):
    class Meta:
        model = Dutyes
        fields = ('employee',
                  'day1','day2','day3','day4','day5',
                  'day6','day7','day8','day9','day10',
                  'day11', 'day12', 'day13', 'day14', 'day15',
                  'day16', 'day17', 'day18', 'day19', 'day20',
                  'day21', 'day22', 'day23', 'day24', 'day25',
                  'day26', 'day27', 'day28', 'day29', 'day30',
                  'day31',
                  )



class UserRegistrationForm(ModelForm):
    password = CharField(label='Пароль', widget=PasswordInput)
    password2 = CharField(label='Повторный ввод пароля', widget=PasswordInput)
    username = CharField(label='Пользователь', initial='')


    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email')
        labels = ('Имя пользователя')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Passwords don\'t match.')
        return cd['password2']