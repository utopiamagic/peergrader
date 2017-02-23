from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group, Permission

# Create your views here.

from .forms import UserForm

class AuthBase :
	def loggedin(request):
		'Returns whether if the user is logged in'
		return request.user.is_authenticated()

	def current_user(request) :
		'Returns current user'
		if request.user.is_authenticated() :
			return request.user
		else :
			return None

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


	def find_all() :
		'Reset the password if the credential is valid'
		user = authenticate(username=uid, password=oldpwd)
		if user is not None:
			u = User.objects.get(username=uid)
			u.set_password(newpwd)
			u.save()
			return True
		else:
			return False

	def update(request):
		'Update the given user with data'
		if request.method == "POST":
			u = UserForm(data=request.POST, instance=request.POST.get('username'))
			if form.is_valid():
				user = form.save(commit=False)
				user.save()
	
	def rename(old_name, new_name) :
		'Update the user\' old UBC ID with the new ID'
		print('Warning: this function does not update the user\'s id in tables other than User')
		u = User.objects.filter(username=old_name).update(username=new_name)
	
	def inactivate(username) :
		'Inactive the user and returns True if succeed'
		u = User.objects.filter(username=username)
		if len(u) == 0 :
			return False
		else :
			u.update(is_active=False).save()
			return True
	
	def set_group(gname, user) :
		'Set the given users group'
		if gname in ('student', 'assistant', 'instructor', 'superuser') :
			stu_group, created = Group.objects.get_or_create(name=gname)
			user.groups.add(stu_group)
			user.save()
		return user

	def get_user_by_group(gname) :
		try :
			users = Group.objects.get(name=gname).user_set.all()
			return users
		except Group.DoesNotExist:
			print("Group.DoesNotExist", gname)
			return None
	
	def find_by_name(name) :
		pass
	
	def find_by_id(uid) :
		return User.objects.get(id=uid)
		
	def promote(uid) :
		u = User.objects.filter(id=uid).update	\
			(is_superuser=True, is_staff=True)
		return u
	
class AuthViews :
	@never_cache
	def user_signup(request):
		'Renders the user signup page'
		render_dict = {
			'is_login': False,
		}
		if request.method == 'POST':
			u = UserForm(data=request.POST)
			if u.is_valid():
				# Save a new user object from the form's data.
				new_user = u.save()
				new_user.set_password(u.cleaned_data['password'])
				new_user.save()
				if request.POST.get("special") is not None :
					AuthBase.set_group(request.POST.get('groups'), new_user)
					print('get a new post!')
					return HttpResponseRedirect('/auth/panel/')
				AuthBase.set_group('student', new_user)
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
		
	@never_cache
	def user_promote(request, uid):
		'Promote the current user'
		render_dict = dict()
		#t = request.GET.get('role')
		AuthBase.promote(uid)
		AuthBase.set_group("superuser", AuthBase.find_by_id(uid))
		render_dict = {
			'good': "",
		}
		#return render(request, 'success.html', render_dict)
		return render(request, 'auth.html', render_dict)
		
	def user_fetch(request) :
		render_dict = dict()
		t = request.GET.get('type')
		if t is not None :
			users = AuthBase.get_user_by_group(t)
			render_dict['users'] = users
			return render(request, 'user-table.html', render_dict)
		else :
			render_dict = {
				#'platform': platform.system() + ' ' + platform.release(),
			}
			return render(request, 'auth.html', render_dict)
	
	def user_inactivate(request) :
		render_dict = dict()
		if request.method == 'POST':
			uname = request.POST.get('username')
			if uname != None :
				AuthBase.inactivate(uname)
				return render(request, 'msg.html', render_dict)
	
	def signup_form(request) :
		render_dict = dict()
		if request.method == 'POST':
			u = UserForm(data=request.POST)
			print(u.errors)
			if u.is_valid():
				# Save a new user object from the form's data.
				new_user = u.save()
				new_user.set_password(u.cleaned_data['password'])
				new_user.save()
				AuthBase.set_group(request.POST.get('groups'), new_user)
				return HttpResponseRedirect('/account/fetch/')
			return HttpResponseRedirect('/account/fetch/')
		else :
			t = request.GET.get('type')
			if t == 'create' :
				return render(request, 'complete-signup.html', render_dict)
			else :
				return render(request, 'rename.html', render_dict)

	def password_change(request):
		if request.method == 'POST':
			form = PasswordChangeForm(user=request.user, data=request.POST)
			if form.is_valid():
				form.save()
				update_session_auth_hash(request, form.user)
		else:
			pass
			
	def user_iden(request, uid) :
		render_dict = dict()
		render_dict['u'] = AuthBase.find_by_id(uid)
		return render(request, 'user-iden.html', render_dict)
