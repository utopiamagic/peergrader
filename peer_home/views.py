from django.shortcuts import render

from peer_course.views import CourseBase

class HomeViews :
	def homepage(request):
		'Render the homepage'
		render_dict = {
			'courses': CourseBase.all(),
		}
		return render(request, 'index.html', render_dict)
