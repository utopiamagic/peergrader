from django import forms
from django.forms import ModelForm
#from django.contrib.admin import widgets

import re

from .models import Assignments, ReviewSettings

#class NameForm(forms.Form):
#	your_name = forms.CharField(label='Your name', max_length=100)


class AssignmentForm(ModelForm):
	class Meta:
		model = Assignments
		fields = ['name',  'browsable', 'passwordmessage', 'password', ] 
		#'courseid'

class ReviewSettingsForm(ModelForm):
	class Meta:
		model = ReviewSettings
		fields = ['showmarksforotherreviews', 'assignmentid', 
		'submissionquestion', 'submissiontype', 'maxsubmissionscore', 
		'maxreviewscore', 'defaultnumberofreviews', 'allowrequestofreviews', 
		'showmarksforreviewsreceived', 'showotherreviewsbystudents', 
		'showotherreviewsbyinstructors', 'showmarksforreviewedsubmissions', 
		'showpoolstatus', 'calibrationmincount', 'calibrationmaxscore',
		'calibrationthresholdmse','calibrationthresholdscore',
		'autoassignessaytopic', 'extracalibrations', 'essaywordlimit', 
		] 

#	def clean_email(self):
#		data = self.cleaned_data['email']
#		if re.match("^([a-zA-Z0-9_\-\.]+)@((ugrad\.cs|alumni|cs){,1}\.)*ubc\.ca$", data) is None:
#			raise forms.ValidationError("UBC Email Address Required")
#		return data


