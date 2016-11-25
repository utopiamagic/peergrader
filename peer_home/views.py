from django.shortcuts import render

from peer_course.views import CourseBase

class HomeViews :
	def homepage(request):
		'Render the homepage'
		render_dict = {
			'courses': CourseBase.all(),
			'logged_in': request.user.is_authenticated(),
		}
		return render(request, 'index.html', render_dict)
