from django import forms
from django.forms import ModelForm
#from django.contrib.admin import widgets

from .models import CourseConfiguration

class CourseConfigurationForm(ModelForm):
	class Meta:
		model = CourseConfiguration
		fields = ['courseid', 'windowsize', 'numreviews', 'maxattempts', 'numcovertcalibrations', 'exhaustedcondition', 'minreviews', 'spotcheckprob', 'highmarkthreshold', 'highmarkbias', 'calibrationthreshold', 'calibrationbias', "scorewindowsize", "scorethreshold", "disqualifywindowsize", "disqualifythreshold", "scorenoise"] 
		#'courseid'


