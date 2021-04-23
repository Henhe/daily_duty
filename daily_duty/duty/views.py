from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from duty.models import CommandLine, SupportLine, Period, Month, WorkHours, Employees, Dutyes
from duty.forms import CommandForm, LineForm, PeriodForm, WorkHoursForm, EmployeeForm, DutyForm, DutyFormReport
from django.contrib import messages
from django.views.generic.base import TemplateView
import datetime
import calendar
from duty.forms import UserRegistrationForm

from django.http import JsonResponse
from .serializers import CommandLineSerializer

import duty.addModule as addM


def is_user_logined(request):
    # breakpoint()
    if not request.user.is_authenticated:
        return False
    else:
        return True

from django.core.mail import send_mail


def get_info(request):

    # send_mail(' Test', ' Test ! !! ', 'oleg.goncharov@servolux.by', ['oleg.goncharov@servolux.by'], html_message=' Test ! ! ! ')
    if is_user_logined(request):
        if request.method == 'POST':
            dict1 = dict(request.POST)

            q = Q(workhours=WorkHours.objects.filter(pk=dict1.pop('periodId')[0])[0])

            filter1 = dict1.pop('commandId')[0]
            if filter1 != '':
                q = q & Q(commandline=CommandLine.objects.filter(pk=filter1)[0])

            filter2 = dict1.pop('supportId')[0]
            if filter2 != '':
                q = q & Q(supportline=SupportLine.objects.filter(pk=filter2)[0])

            dut = Dutyes.objects.filter(q)

        else:
            q = Q(workhours=WorkHours.objects.filter(pk=Period.objects.all()[0].pk)[0])
            dut = Dutyes.objects.filter(q)

        bbs = []
        numbers = []
        for dut_ in dut:
            bbs.append(dut_.get_info_for_index())
            numbers = [str(i) for i in range(1, dut_.workhours.days_quantity + 1)]

        _periods = WorkHours.objects.all()
        _commands = CommandLine.objects.all()
        _supports = SupportLine.objects.all()

        return render(request, "duty/dutyes_report.html", {'bbs': bbs,
                                                           'numbers': numbers,
                                                           'periods': _periods,
                                                           'commands': _commands,
                                                           'supports': _supports
                                                           })
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


# @login_required(login_url='/accounts/login/')
def edit_common(request, table_name, _id, _mode, return_to_index='0'):
    print(f'{table_name} {_id} {_mode} {return_to_index}')
    if is_user_logined(request):
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
            return edit_dutyes(request, _id, _mode, return_to_index)
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


# @login_required(login_url='/accounts/login/')
def commands(request):
    if is_user_logined(request):
        bbs = CommandLine.objects.all()
        context = {'bbs': bbs}
        return render(request, 'duty/commands.html', context)
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


# @login_required(login_url='/accounts/login/')
def edit_command(request, command_line_id, command_line_mode):
    if is_user_logined(request):
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
                    return render(request, "duty/create_command.html", {'form': form, "type_command": type_command})
            else:
                form = CommandForm(instance=command)
                return render(request, "duty/create_command.html", {'form': form, "type_command": type_command})
        elif command_line_mode == 'del':
            command = CommandLine.objects.get(pk=command_line_id)
            command.delete()
            return HttpResponseRedirect(reverse_lazy('commands'))
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


# @login_required(login_url='/accounts/login/')
def lines(request):
    if is_user_logined(request):
        bbs = SupportLine.objects.all()
        context = {'bbs': bbs}
        return render(request, 'duty/lines.html', context)
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


# @login_required(login_url='/accounts/login/')
def edit_line(request, line_id, line_mode):
    if is_user_logined(request):
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
                    # messages.success(request, 'Support line added succesfully')
                    return HttpResponseRedirect(reverse_lazy('lines'))
                else:
                    messages.error(request, 'Support line save error, please check fields below')
                    return render(request, "duty/create_line.html", {'form': form, "type_command": type_command})
            else:
                form = LineForm(instance=line)
                return render(request, "duty/create_line.html", {'form': form, "type_command": type_command})
        elif line_mode == 'del':
            line = SupportLine.objects.get(pk=line_id)
            line.delete()
            return HttpResponseRedirect(reverse_lazy('lines'))
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


# @login_required(login_url='/accounts/login/')
def employees(request):
    if is_user_logined(request):
        bbs = Employees.objects.all()
        context = {'bbs': bbs}
        return render(request, 'duty/employees.html', context)
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


# @login_required(login_url='/accounts/login/')
def edit_employee(request, employee_id, employee_mode):
    if is_user_logined(request):
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
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


# @login_required(login_url='/accounts/login/')
def periods(request):
    if is_user_logined(request):
        bbs = Period.objects.all()
        context = {'bbs': bbs}
        return render(request, 'duty/periods.html', context)
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


# @login_required(login_url='/accounts/login/')
def edit_period(request, period_id, period_mode):
    if is_user_logined(request):
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
                    # messages.success(request, 'Period added succesfully')
                    messages.add_message(request, 80, 'Period added succesfully')
                    return HttpResponseRedirect(reverse_lazy('periods'))
                else:
                    # messages.error(request, 'Period save error, please check fields below')
                    messages.add_message(request, 80, 'Period save error, please check fields below')
                    return render(request, "duty/create_period.html", {'form': form, "type_command": type_command})
            else:
                form = PeriodForm(instance=period)
                return render(request, "duty/create_period.html", {'form': form, "type_command": type_command})

        elif period_mode == 'del':
            period = Period.objects.get(pk=period_id)
            period.delete()
            return HttpResponseRedirect(reverse_lazy('periods'))
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


# @login_required(login_url='/accounts/login/')
def workhours(request):
    if is_user_logined(request):
        bbs = WorkHours.objects.all()
        context = {'bbs': bbs}
        return render(request, 'duty/workhours.html', context)
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


# @login_required(login_url='/accounts/login/')
def edit_workhours(request, workhours_id, workhours_mode):
    if is_user_logined(request):
        if workhours_mode == 'edit':
            if int(workhours_id):
                wh = WorkHours.objects.get(pk=workhours_id)
                type_command = 'Редактирование '
            else:
                wh = WorkHours()
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

                        wh.save_hours(dict1)
                    messages.success(request, 'Working hours added succesfully')
                    return HttpResponseRedirect(reverse_lazy('workhours'))
                else:
                    messages.error(request, 'Working hours save error, please check fields below')
            else:

                form = WorkHoursForm(instance=wh)

                first_list = [{'0': ''}, {'0': ''}, {'0': ''}, {'0': ''}, {'0': ''}, {'0': ''}]
                if int(workhours_id):
                    begin_month = datetime.date(wh.period.year, wh.period.month.name_int, 1).weekday()
                    days_in_month = calendar.mdays[wh.period.month.name_int]

                    if calendar.isleap(wh.period.year) and wh.period.month.name_int == 2:
                        days_in_month = days_in_month + 1
                    reslist = []

                    reslist.extend(first_list[:begin_month])
                    reslist.extend(wh.get_days_as_list_of_dict()[:days_in_month])
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
            wh = WorkHours.objects.get(pk=workhours_id)
            wh.delete()
            return HttpResponseRedirect(reverse_lazy('workhours'))
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


# @login_required(login_url='/accounts/login/')
def dutyes(request):
    if is_user_logined(request):
        bbs = Dutyes.objects.all()
        context = {'bbs': bbs}
        return render(request, 'duty/dutyes.html', context)
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


# @login_required(login_url='/accounts/login/')
def edit_dutyes(request, duty_id, duty_mode, return_to_index):
    if is_user_logined(request):
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
                    # return_to_index = dict1.pop('return_to_index')[0]
                    dict1.pop('workhours')
                    dict1.pop('employee')
                    dict1.pop('commandline')
                    dict1.pop('supportline')
                    # dict1.pop('days_quantity')
                    dict1.pop('csrfmiddlewaretoken')
                    # print(dict1)
                    # breakpoint()
                    # print(f'return_to_index {return_to_index}')
                    duty.save_hours(dict1)
                    messages.success(request, 'Duty added succesfully')
                    if return_to_index == '1':
                        return HttpResponseRedirect(reverse_lazy('index'))
                    else:
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
                                                                 'numbers': numbers,
                                                                 'return_to_index': return_to_index})
        elif duty_mode == 'del':
            duty = Dutyes.objects.get(pk=duty_id)
            duty.delete()
            return HttpResponseRedirect(reverse_lazy('dutyes'))
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'user_form': user_form,
                                                              'user': '',
                                                              'password': ''})


def api_commandsline(request):
    if request.method == 'GET':
        commands_ = CommandLine.objects.all()
        serializer = CommandLineSerializer(commands_, many=True)
        return JsonResponse(serializer.data, safe=False)


def api_duty_data(request, _type_duty, _day, _month, _year):
    if request.method == 'GET':
        q = Q(month=Month.objects.filter(name_int=_month)[0]) & Q(year=_year)
        dict_ = dict()
        answer = ''
        value = Period.objects.filter(q)
        if len(value) > 0:
            period = value[0]
            value = WorkHours.objects.filter(period=period)
            if len(value) > 0:
                wh = value[0]
                name = f'day{_day}'
                duty = Dutyes.objects.filter(workhours=wh)
                for i in duty:
                    if i.__getattribute__(name):
                        if i.commandline is not None:
                            dict_[i.commandline.name] = i.employee.full_name()
                        if i.supportline is not None:
                            dict_[i.supportline.name] = i.employee.full_name()
            else:
                answer = 'Empty workhours'
        else:
            answer = "Don't find period"
        if len(dict_) == 0 and answer == '':
            answer = 'No dutyes'

        if len(dict_) > 0:
            return JsonResponse(dict, safe=False)
        else:
            return JsonResponse(answer, safe=False)


def fill_duty(request):

    # send_mail(' Test', ' Test ! !! ', 'oleg.goncharov@servolux.by', ['oleg.goncharov@servolux.by'], html_message=' Test ! ! ! ')
    if is_user_logined(request):
        command_ = -1
        support_ = -1
        period_ = -1
        if request.method == 'POST':
            dict1 = dict(request.POST)
            q = None

            filter0 = dict1.pop('periodId')[0]
            if filter0 != '':
                period_ = filter0
                if q is not None:
                    q = q & Q(workhours=WorkHours.objects.filter(pk=filter0)[0])
                else:
                    q = Q(workhours=WorkHours.objects.filter(pk=filter0)[0])


            filter1 = dict1.pop('commandId')[0]
            if filter1 != '':
                command_ = filter1
                if q is not None:
                    q = q & Q(commandline=CommandLine.objects.filter(pk=filter1)[0])
                else:
                    q = Q(commandline=CommandLine.objects.filter(pk=filter1)[0])

            filter2 = dict1.pop('supportId')[0]
            if filter2 != '':
                support_ = filter2
                if q is not None:
                    q = q & Q(supportline=SupportLine.objects.filter(pk=filter2)[0])
                else:
                    q = Q(supportline=SupportLine.objects.filter(pk=filter2)[0])

            if filter1 or filter2:
                dut = Dutyes.objects.filter(q)
            else:
                dut = Dutyes.objects.filter(pk = -1)

        else:
            q = Q(workhours=WorkHours.objects.filter(pk=Period.objects.all()[0].pk)[0])
            # dut = Dutyes.objects.filter(q)
            dut = Dutyes.objects.filter(pk=-1)

        # print(f'{period_}{command_}{support_}')
        bbs = []
        numbers = []
        _employees = []
        if len(dut) > 0:
            have_data = True
        else:
            have_data = False

        for dut_ in dut:
            bbs.append(dut_.get_info_for_index())
            numbers = [str(i) for i in range(1, dut_.workhours.days_quantity + 1)]
            _employees.append(dut_.employee)

        _periods = WorkHours.objects.all()
        _commands = CommandLine.objects.all()
        _supports = SupportLine.objects.all()

        return render(request, "duty/fill_duty.html", {'bbs': bbs,
                                                           'numbers': numbers,
                                                           'periods': _periods,
                                                           'commands': _commands,
                                                           'supports': _supports,
                                                           'period': period_,
                                                           'command': command_,
                                                           'support': support_,
                                                           'employees': _employees,
                                                           'have_data': have_data
                                                           })
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)