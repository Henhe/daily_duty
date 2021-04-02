from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from duty.models import CommandLine, SupportLine, Period, Month, WorkHours, Employees, Dutyes
from duty.forms import CommandForm, LineForm, PeriodForm, WorkHoursForm, EmployeeForm, DutyForm
from django.contrib import messages
from django.views.generic.base import TemplateView
import datetime
import calendar


def index(request):
    # s = ''
    # for month in Month.objects.filter(name_int__gte = 5):
    # 	s += month.name + str(month.name_int) + '\n'
    # month = Month.objects.get(pk = 1)
    # period = Period.objects.get(month = month, year = 2021)
    # wh = WorkHours.objects.get(period = period)
    # return HttpResponse(str(wh))
    # return render(request, 'duty/index.html ', context)
    return render(request, 'duty/index.html')


def edit_common(request, table_name, _id, _mode):
    if table_name == 'commands':
        return edit_command(request, _id, _mode)
    elif table_name == 'lines':
        return edit_line(request, _id, _mode)
    elif table_name == 'periods':
        return edit_period(request, _id, _mode)
    elif table_name == 'workhours':
        return edit_workhours(request, _id, _mode)
    elif table_name == 'employees':
        return edit_employee(request, _id, _mode)
    elif table_name == 'dutyes':
        return edit_dutyes(request, _id, _mode)


def commands(request):
    bbs = CommandLine.objects.all()
    context = {'bbs': bbs}
    return render(request, 'duty/commands.html', context)


def edit_command(request, command_line_id, command_line_mode):
    if command_line_mode == 'edit':
        if int(command_line_id):
            command = CommandLine.objects.get(pk=command_line_id)
            type_command = 'Редактирование '
        else:
            command = CommandLine()
            type_command = 'Создание '

        if request.method == 'POST':
            form = CommandForm(request.POST, instance=command)
            if form.is_valid():
                form.save()
                messages.success(request, 'Command added succesfully')
                return HttpResponseRedirect(reverse_lazy('commands'))
            else:
                messages.error(request, 'Command save error, please check fields below')
        else:
            form = CommandForm(instance=command)
            return render(request, "duty/create_command.html", {'form': form, "type_command": type_command})
    elif command_line_mode == 'del':
        command = CommandLine.objects.get(pk=command_line_id)
        command.delete()
        return HttpResponseRedirect(reverse_lazy('commands'))


def lines(request):
    bbs = SupportLine.objects.all()
    context = {'bbs': bbs}
    return render(request, 'duty/lines.html', context)


def edit_line(request, line_id, line_mode):
    if line_mode == 'edit':
        if int(line_id):
            line = SupportLine.objects.get(pk=line_id)
            type_command = 'Редактирование '
        else:
            line = SupportLine()
            type_command = 'Создание '
        #
        if request.method == 'POST':
            form = LineForm(request.POST, instance=line)
            if form.is_valid():
                form.save()
                messages.success(request, 'Support line added succesfully')
                return HttpResponseRedirect(reverse_lazy('lines'))
            else:
                messages.error(request, 'Support line save error, please check fields below')
        else:
            form = LineForm(instance=line)
            return render(request, "duty/create_line.html", {'form': form, "type_command": type_command})
    elif line_mode == 'del':
        line = SupportLine.objects.get(pk=line_id)
        line.delete()
        return HttpResponseRedirect(reverse_lazy('lines'))


def employees(request):
    bbs = Employees.objects.all()
    context = {'bbs': bbs}
    return render(request, 'duty/employees.html', context)


def edit_employee(request, employee_id, employee_mode):
    if employee_mode == 'edit':
        if int(employee_id):
            employee = Employees.objects.get(pk=employee_id)
            type_command = 'Редактирование '
        else:
            employee = Employees()
            type_command = 'Создание '
        #
        if request.method == 'POST':
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
                messages.success(request, 'Employee added succesfully')
                return HttpResponseRedirect(reverse_lazy('employees'))
            else:
                messages.error(request, 'Employee save error, please check fields below')
        else:
            form = EmployeeForm(instance=employee)
            return render(request, "duty/create_employee.html", {'form': form, "type_command": type_command})
    elif employee_mode == 'del':
        employee = Employees.objects.get(pk=employee_id)
        employee.delete()
        return HttpResponseRedirect(reverse_lazy('employees'))


def periods(request):
    bbs = Period.objects.all()
    context = {'bbs': bbs}
    return render(request, 'duty/periods.html', context)


def edit_period(request, period_id, period_mode):
    if period_mode == 'edit':
        if int(period_id):
            period = Period.objects.get(pk=period_id)
            type_command = 'Редактирование '
        else:
            period = Period()
            type_command = 'Создание '

        if request.method == 'POST':
            form = PeriodForm(request.POST, instance=period)
            if form.is_valid():
                form.save()
                messages.success(request, 'Period added succesfully')
                return HttpResponseRedirect(reverse_lazy('periods'))
            else:
                messages.error(request, 'Period save error, please check fields below')
        else:
            form = PeriodForm(instance=period)
            return render(request, "duty/create_period.html", {'form': form, "type_command": type_command})

    elif period_mode == 'del':
        period = Period.objects.get(pk=period_id)
        period.delete()
        return HttpResponseRedirect(reverse_lazy('periods'))


def workhours(request):
    bbs = WorkHours.objects.all()
    context = {'bbs': bbs}
    return render(request, 'duty/workhours.html', context)


def edit_workhours(request, workhours_id, workhours_mode):
    if workhours_mode == 'edit':
        if int(workhours_id):
            workhours = WorkHours.objects.get(pk=workhours_id)
            type_command = 'Редактирование '
        else:
            workhours = WorkHours()
            type_command = 'Создание '

        if request.method == 'POST':

            form = WorkHoursForm(request.POST, instance=workhours)
            if form.is_valid():
                form.save()
                if int(workhours_id):
                    dict1 = dict(request.POST)

                    dict1.pop('period')
                    dict1.pop('days_quantity')
                    dict1.pop('csrfmiddlewaretoken')

                    workhours.save_hours(dict1)
                messages.success(request, 'Working hours added succesfully')
                return HttpResponseRedirect(reverse_lazy('workhours'))
            else:
                messages.error(request, 'Working hours save error, please check fields below')
        else:

            form = WorkHoursForm(instance=workhours)

            first_list = [{'0': ''}, {'0': ''}, {'0': ''}, {'0': ''}, {'0': ''}, {'0': ''}]
            if int(workhours_id):
                begin_month = datetime.date(workhours.period.year, workhours.period.month.name_int, 1).weekday()
                days_in_month = calendar.mdays[workhours.period.month.name_int]

                if calendar.isleap(workhours.period.year) and workhours.period.month.name_int == 2:
                    days_in_month = days_in_month + 1
                reslist = []

                reslist.extend(first_list[:begin_month])
                reslist.extend(workhours.get_days_as_list_of_dict()[:days_in_month])
                reslist.extend(first_list[:43 - len(reslist)])
                return render(request, "duty/create_workhours.html", {'form': form,
                                                                      'wh_id': workhours_id,
                                                                      'type_command': type_command,
                                                                      'week1': reslist[0:7],
                                                                      'week2': reslist[7:14],
                                                                      'week3': reslist[14:21],
                                                                      'week4': reslist[21:28],
                                                                      'week5': reslist[28:35],
                                                                      'week6': reslist[35:42],
                                                                      'visible_dates': True
                                                                      })
            else:
                return render(request, "duty/create_workhours.html", {'form': form,
                                                                      'wh_id': workhours_id,
                                                                      'type_command': type_command,
                                                                      'week1': None,
                                                                      'week2': None,
                                                                      'week3': None,
                                                                      'week4': None,
                                                                      'week5': None,
                                                                      'week6': None,
                                                                      'visible_dates': False
                                                                      })

    elif workhours_mode == 'del':
        workhours = WorkHours.objects.get(pk=workhours_id)
        workhours.delete()
        return HttpResponseRedirect(reverse_lazy('workhours'))


def dutyes(request):
    bbs = Dutyes.objects.all()
    context = {'bbs': bbs}
    return render(request, 'duty/dutyes.html', context)


def edit_dutyes(request, duty_id, duty_mode):
    if duty_mode == 'edit':
        if int(duty_id):
            duty = Dutyes.objects.get(pk=duty_id)
            type_command = 'Редактирование '
        else:
            duty = Dutyes()
            type_command = 'Создание '
        #
        if request.method == 'POST':
            form = DutyForm(request.POST, instance=duty)
            if form.is_valid():
                form.save()
                dict1 = dict(request.POST)

                dict1.pop('workhours')
                dict1.pop('employee')
                dict1.pop('commandline')
                dict1.pop('supportline')
                # dict1.pop('days_quantity')
                dict1.pop('csrfmiddlewaretoken')
                print(dict1)
                # breakpoint()
                duty.save_hours(dict1)
                messages.success(request, 'Duty added succesfully')
                return HttpResponseRedirect(reverse_lazy('dutyes'))
            else:
                messages.error(request, 'Duty save error, please check fields below')
        else:
            form = DutyForm(instance=duty)
            if int(duty_id):
                values = duty.get_days_as_list_of_dict()
                numbers = [str(i) for i in range(1, duty.workhours.days_quantity + 1)]
            else:
                values = [{f'day{i}': False} for i in range(1, 32)]
                numbers = [str(i) for i in range(1, 32)]

            # breakpoint()
            return render(request, "duty/create_duty.html", {'form': form,
                                                             "type_command": type_command,
                                                             'values': values,
                                                             'numbers': numbers})
    elif duty_mode == 'del':
        duty = Dutyes.objects.get(pk=duty_id)
        duty.delete()
        return HttpResponseRedirect(reverse_lazy('dutyes'))
