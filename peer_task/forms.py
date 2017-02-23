from django import forms
from django.forms import ModelForm
#from django.contrib.admin import widgets

import re

from .models import Assignments

#class NameForm(forms.Form):
#	your_name = forms.CharField(label='Your name', max_length=100)


class AssignmentForm(ModelForm):
	class Meta:
		model = Assignments
		fields = ['name',  'browsable', 'passwordmessage', 'password', ] 
		#'courseid'


