from django.shortcuts import render
from django.http import HttpResponseRedirect
from peer_course.views import CourseBase
from peer_auth.views import AuthBase
#import platform

# Functions other than view functions should be placed elsewhere

class PanelViews() :
	def doo(request):
		'Render the homepage'
		#if request.user.is_authenticated() :
		return render(request, 'index.html')

	def homepage(request):
		'Render the homepage'
		render_dict = {
			'courses': CourseBase.all(),
			'logged_in': request.user.is_authenticated(),
		}
		if request.user.is_authenticated():
			render_dict['lastname'] = request.user.last_name
			render_dict['firstname'] = request.user.first_name
			return HttpResponseRedirect("/course/all/")
		return render(request, 'index.html', render_dict)
