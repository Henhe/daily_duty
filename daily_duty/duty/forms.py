from django.forms import ModelForm
from .models import CommandLine

class CommandForm(ModelForm):
	class Meta:
		model = CommandLine
		fields = ('name',)