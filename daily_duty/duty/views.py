from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse


from duty.models import Month
from duty.models import Period
from duty.models import WorkHours
from duty.models import CommandLine


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

def commands(request):
	# bbs = Bb.objects.filter(rubric=rubric_id)
	# rubrics = Rubric.objects.all()
	# current_rubric = Rubric.objects.get(pk=rubric_id)
	# context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
	# return render(request, 'bboard/by_rubric.html', context)
	bbs = CommandLine.objects.all()
	context = {'bbs': bbs}
	return render(request, 'duty/commands.html', context)
	# return render(request, 'duty/index.html')

def addcommands(request):

	return HttpResponse(str(1))

# from django.views.generic.edit import FormView
from .forms import CommandForm
from django.urls import reverse_lazy
#
# class Commands_add_edit(FormView):
# 	template_name = 'duty/create_command.html'
# 	form_class = CommandForm
# 	success_url = reverse_lazy('commands')
#
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['name'] = self.kwargs.get('command_line_id', 'unknown')
# 		# print(**kwargs['id'])
# 		return context





def edit_command(request, command_line_id):

	if int(command_line_id):
		command = CommandLine.objects.get(pk=command_line_id)
	else:
		command = CommandLine()
	#
	if request.method == 'POST':
	 	form = CommandForm(request.POST, instance=command)
	 	if form.is_valid():
	 		form.save()
	 		# messages.success(request, 'Command added succesfully')
	 		return HttpResponseRedirect(reverse_lazy('commands'))
	 	# else:
	 		# messages.error(request, 'Command save error, please check fields below')
	else:
		form = CommandForm(instance = command)
		return render(request, "duty/create_command.html", {'form': form})


	# return HttpResponse(str(context_))
def lines(request):
	return render(request, 'duty/lines.html')


def staff(request):
	return render(request, 'duty/staff.html')


def periods(request):
	return render(request, 'duty/periods.html')


def dutyes(request):
	return render(request, 'duty/dutyes.html')

