from django.shortcuts import render

from peer_course.views import CourseBase
from peer_auth.views import AuthBase

# Functions other than view functions should be placed elsewhere

class HomeViews :
	def homepage(request):
		'Render the homepage'
		render_dict = {
			'courses': CourseBase.all(),
			'logged_in': request.user.is_authenticated(),
		}
		if request.user.is_authenticated():
			render_dict['lastname'] = request.user.lastname
			render_dict['firstname'] = request.user.firstname
		return render(request, 'index.html', render_dict)
		
	def auth_panel(request) :
		return render(request, 'auth.html')
