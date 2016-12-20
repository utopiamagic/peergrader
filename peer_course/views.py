from django.shortcuts import render
from .models import *
import uuid
# Create your views here.

class CourseBase :
	def create(name, browsable, archived) :
		c = CourseList(displayname=name, browsable=browsable, archived=archived)
		c.stucode = str(uuid.uuid3(uuid.NAMESPACE_DNS, name + "/STU"))[0:8]
		c.tascode = str(uuid.uuid3(uuid.NAMESPACE_DNS, name + "/TAS"))[0:8]
		c.save()
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
		
	def all() :
		result = CourseList.objects.all()
		return result
	
	def is_member(user) :
		return True
	
	def identity(cid, code) :
		c = CourseList.objects.filter(courseid=cid).first()
		if c is None :
			return "invalid"
		elif cid == c.stucode :
			return "stucode"
		elif cid == c.tascode :
			return "tascode"
		else :
			return "invalid"
			
	def add_user(cid, uid) :
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
	
	def enroll(cid, user) :
		c = CourseList.objects.filter(courseid=cid).first()
		u = Users.objects.filter(id=uid).first()
		pass

class CourseViews :
	def access(request, cid) :
		if request.method == 'POST' :
			pass
		else :
			return render(request, 'course.html')

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
			c = CourseBase.create(cname, browsable, archived)
			if c is not None :
				render_dict['success'] = True
			return render(request, 'create-course.html', render_dict)
		
	def listing(request) :
		if request.method == 'POST' :
			pass
		else :
			render_dict = dict()
			render_dict["clist"] = CourseBase.all()
			return render(request, 'courses-list.html', render_dict)
			
	def add_user(request) :
		if request.method == 'POST' :
			pass
			
	def modify(request, cid) :
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
			else :
				render_dict["error"] = "Error?"
			return render(request, 'success-msg.html', render_dict)
