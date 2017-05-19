from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
#from django.contrib.auth.models import User
from peer_auth.views import AuthBase
import uuid
# Create your views here.

from .forms import CourseConfigurationForm

class CourseBase :
	def create(user, name, browsable, archived) :
		"Create the course and add the current user as the instructor"
		sname = name.lower().replace(' ', '')
		c = CourseList(displayname=name, name=sname, browsable=browsable, archived=archived)
		c.stucode = str(uuid.uuid3(uuid.NAMESPACE_DNS, name + "/STU"))[0:8]
		c.tascode = str(uuid.uuid3(uuid.NAMESPACE_DNS, name + "/TAS"))[0:8]
		#c.instructor = user
		c.save()
		ins = CourseMember(courseid=c.courseid, userid=user.id, usertype='instructor')
		ins.save()
		return c
	
	def archive(cid) :
		c = CourseList.objects.filter(courseid=cid).update(archived=True)
		return c
	
	def show(cid) :
		c = CourseList.objects.filter(courseid=cid).update(browsable=True)
		return c

	def hide(cid) :
		c = CourseList.objects.filter(courseid=cid).update(browsable=False)
		return c
		
	def delete(cid) :
		CourseList.objects.filter(courseid=cid).delete()
		CourseMember.objects.filter(courseid=cid).delete()
			
	def all() :
		result = CourseList.objects.all()
		return result
	
	def is_member(user) :
		return True

	def is_instructor(user) :
		cm = CourseMember.objects.filter(userid=user.id)
		return cm.exists()
		
	def exists(dname) :
		c = CourseList.objects.filter(displayname=dname)
		print(c.exists())
		return c.exists()
	
	def enroll(user, code) :
		"takes a user and a course code and see whether if the relevant role exists"
		print(user.id)

		#print("course",c)
		c = CourseList.objects.filter(stucode=code).first()
		if c is not None :
			print("A valid student code")
			c = CourseList.objects.filter(stucode=code).first()
			assert(not CourseMember.objects.filter(courseid=c.courseid, userid=user.id).exists())
			cm = CourseMember(courseid=c.courseid, userid=user.id, usertype='student')
			cm.save()
			return cm
		c = CourseList.objects.filter(tascode=code).first()
		if c is not None :
			print("A valid TA code")
			c = CourseList.objects.filter(tascode=code).first()
			assert(not CourseMember.objects.filter(courseid=c.courseid, userid=user.id).exists())
			cm = CourseMember(courseid=c.courseid, userid=user.id, usertype='grader')
			cm.save()
			return cm
		print("code x match")
		return None

	def add_user_by_id(cid, uid) :
		c = CourseList.objects.filter(courseid=cid).first()
		u = Users.objects.filter(id=uid).first()
		if c is None or u is None :
			return False
		elif u in c.users.all() :
			return True
		else :
			c.users.add(u)
			c.save()
			return c
	
	def set_instructor(cid, user) :
		c = CourseMember.objects.filter(courseid=cid, userid=user.id).first()
		# is the role of the two same?
		if c is not None :
			return False
		if not user.is_staff :
			user.is_staff = True 
			user.save()
			print("error: not staff")
		cm = CourseMember(courseid=cid, userid=u.id, usertype="instructor")
		cm.save()
		return cm
	
	def delist(cid, user) :
		m = CourseMember.objects.filter(courseid=cid, userid=user.id)
		if m is not None :
			m.remove()
			return True
		else :
			return False
			
	def find_enrolled_courses(uid, role="student") :
		cl = []
		cm = CourseMember.objects.filter(userid=uid, usertype=role)
		for entry in cm :
			print(entry)
			cl.append(CourseList.objects.get(courseid=entry.courseid))
		return cl

	def get_member(cid, role='student') :
		userlist = []
		cms = CourseMember.objects.filter(courseid=cid, usertype=role)
		if cms is None :
			return userlist
		for u in cms :
			userlist.append(User.objects.get(id=u.userid))
		print(userlist)
		return userlist
		
	def identity(cid, uid) :
		cm =  CourseMember.objects.filter(courseid=cid, userid=uid)[0]
		return cm.usertype
	
	def find_by_name(cname) :
		c = CourseList.objects.filter(displayname=cname)
		return c

	def find_by_id(cid) :
		c = CourseList.objects.get(courseid=cid)
		return c

class CourseViews :

	def config(request, cid):
		if request.user.is_authenticated() is False :
			return HttpResponseRedirect('/account/login/')
		# if this is a POST request we need to process the form data
		cs = CourseList.objects.get(courseid=cid)
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = CourseConfigurationForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				new_conf = form.save()
				new_conf.save()
				# process the data in form.cleaned_data as required
				# redirect to a new URL:
				return HttpResponseRedirect('/course/all/?ok')
			return render(request, 'course-config.html', {'CCfForm': form, 'c':cs, 'cid': cid, 'error':"t",})
		# if a GET (or any other method) we'll create a blank form
		else:
			if CourseConfiguration.objects.filter(courseid=cid).exists() :
				article = CourseConfiguration.objects.get(courseid=cid)
				form = CourseConfigurationForm(instance=article)
			else :
				form = CourseConfigurationForm(initial={'courseid': cid}, )
			return render(request, 'course-config.html', {'CCfForm': form, 'cid': cid, 'c':cs,})


	def view(request, cid):
		if request.user.is_authenticated() is False :
			return HttpResponseRedirect('/account/login/')
		# if a GET (or any other method) we'll create a blank form
		else:
			cs = CourseList.objects.get(courseid=cid)
			return render(request, 'course.html', {'cid': cid, 'c':cs,})

	def create(request) :
		if request.method == 'POST' :
			render_dict = dict()
			cname = request.POST.get('cname')
			browsable = False
			archived = False
			if request.POST.get('browsable') == "true" :
				browsable = True
			if request.POST.get('archived') == "true" :
				archived = True	
			if CourseBase.exists(cname) :
				render_dict['success'] = False
				render_dict['error'] = "Course name conflict"
				return render(request, 'create-course.html', render_dict)
			c = CourseBase.create(request.user, cname, browsable, archived)
			if c is not None :
				ci = CourseBase.set_instructor(c.courseid, request.user)
				render_dict['success'] = True
				render_dict['course'] = c
			return render(request, 'create-course.html', render_dict)
		
	def list_specific(request) :
		"List all the courses of a certain instructor or a student"
		render_dict = dict()
		if request.method == 'POST' :
			pass
		else :
			if not request.user.is_authenticated() :
				return HttpResponseRedirect("/account/login/")
			render_dict["u"] = request.user
			if request.user.is_staff :
				render_dict["admin"] = True
				render_dict["clist"] = CourseBase.all()
				print(render_dict["clist"])
			else :
				render_dict["clist"] = CourseBase.find_enrolled_courses(request.user.id)
				print(CourseMember.objects.filter(userid=request.user.id))
			return render(request, 'courses-list.html', render_dict)

	def list_brief(request) :
		"List a list of courses without specific information"
		render_dict = dict()
		if request.method == 'POST' :
			pass
		else :
			if not request.user.is_authenticated() :
				return HttpResponseRedirect("/account/login/")
			render_dict["u"] = request.user
			if request.user.is_staff :
				render_dict["admin"] = True
				render_dict["clist"] = CourseBase.all()
				print(render_dict["clist"])
			else :
				render_dict["clist"] = CourseBase.find_enrolled_courses(request.user.id)
				print(CourseMember.objects.filter(userid=request.user.id))
			return render(request, 'courses-list.html', render_dict)
			
	def enroll(request) :
		render_dict = dict()
		#render_dict['cid'] = cid
		if request.method == 'POST' :
			code = request.POST.get('coursecode')
			if code == '' :
				return HttpResponseRedirect("/course/all/")
			cm = CourseBase.enroll(request.user, code)
			if cm is not None :
				render_dict['success'] = True
				render_dict['member'] = cm
				print("cid", cm.courseid)
				return HttpResponseRedirect("/course/%s/" % cm.courseid)
			render_dict['error'] = "Please try again"
		return HttpResponseRedirect("/course/all/")
		#return HttpResponseRedirect('/')
			
	def modify(request, cid) :
		"Config the course"
		if request.method == 'POST' :
			pass
		else :
			render_dict = dict()
			action = request.GET.get('action')
			if action == "archive" :
				CourseBase.archive(cid)
			elif action == "hide" :
				CourseBase.hide(cid)
			elif action == "show" :
				CourseBase.show(cid)
			elif action == "delete" :
				render_dict["error"] = "Deleted."
				CourseBase.delete(cid)
			else :
				render_dict["error"] = "Error?"
			return render(request, 'success-msg.html', render_dict)
			
	def members(request, cid) :
		"returns all the members of the class"
		cgs = []
		
		for role in ("student", "grader", "instructor") :
			group = dict()
			group["name"] = role
			group["members"] = CourseBase.get_member(cid, role)
			cgs.append(group)
		
		render_dict = {
			'c': CourseBase.find_by_id(cid),
			'groups': cgs,
		}
		#print(cgs[0].members[0])
		return render(request, 'users-list.html', render_dict)
