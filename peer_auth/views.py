from django.shortcuts import render

# Create your views here.

class AuthBase :
	def test() :
		pass
		
class AuthViews :
	def main(request):
		'Render the login/sign up page'
		render_dict = {
			'pg': '!',
		#	'courses': CourseBase.all(),
		}
		return render(request, 'account.html', render_dict)
