from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

import re

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'email', 'first_name', 'last_name']

	def clean_email(self):
		data = self.cleaned_data['email']
		if re.match("^([a-zA-Z0-9_\-\.]+)@(ugrad\.cs|alumni|cs){,1}\.ubc\.ca$", data) is None:
			raise forms.ValidationError("UBC Email Address Required")
		return data
		
	def clean_username(self):
		data = self.cleaned_data['username']
		if re.match("\d{7,8}", data) is None:
			raise forms.ValidationError("Student ID is not correct")
		return data

