from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

from .forms import UserForm

class AuthBase :
	def loggedin(request):
		'Returns whether if the user is logged in'
		return request.user.is_authenticated()

	def find(request) :
		'Returns current user'
		if request.user.is_authenticated() :
			return request.user
		else :
			return None

	def find_by_name(name) :
		pass
	
	def reset_password(uid, oldpwd, newpwd) :
		'Reset the password if the credential is valid'
		user = authenticate(username=uid, password=oldpwd)
		if user is not None:
			u = User.objects.get(username=uid)
			u.set_password(newpwd)
			u.save()
			return True
		else:
			return False

class AuthViews :
	@never_cache
	def user_signup(request):
		'Renders the user signup page'
		render_dict = {
			'is_login': False,
		}
		if request.method == 'POST':
			print("Received a post!")
			u = UserForm(request.POST)
			if u.is_valid():
				# Save a new user object from the form's data.
				new_user = u.save()
				new_user.set_password(u.cleaned_data['password'])
				new_user.save()
				return HttpResponseRedirect('/account/login/?success=true;')
		else :
			return render(request, 'account.html', render_dict)

	@never_cache
	def user_login(request):
		'Render the login page'
		if request.method == 'POST':
			uid = request.POST['username']
			pwd = request.POST['password']
			user = authenticate(username=uid, password=pwd)
			if user is not None:
				print('successed')
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				print('failed')
		render_dict = dict()
		render_dict['is_login'] = True
		render_dict['is_success'] = request.GET.get('success', None)
		return render(request, 'account.html', render_dict)
		
	@never_cache
	def user_logout(request):
		'Logout the currect session'
		logout(request)
		return HttpResponseRedirect('/')
