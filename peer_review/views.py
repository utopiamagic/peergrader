from django.shortcuts import render
from django.http import HttpResponseRedirect
#from .forms import NameForm
# Create your views here.

from .forms import AssignmentForm, ReviewSettingsForm

class ReviewBase() :
	def create_radio(qid, index, l, scr) :
		ro = ReviewRadioOptions(questionid=qid, index=index, 
			label=l, score=scr)

class ReviewView() :
	def create(request) :
		return render('test.html')

	def get_name(request):
		# if this is a POST request we need to process the form data
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = NameForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				# process the data in form.cleaned_data as required
				# redirect to a new URL:
				return HttpResponseRedirect('/thanks/')
		# if a GET (or any other method) we'll create a blank form
		else:
			form = NameForm()
		return render(request, 'name.html', {'form': form})

