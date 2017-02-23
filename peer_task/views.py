from django.shortcuts import render

# Create your views here.

class TaskBase() :
	def create(cid, name="Assignment #", browsable=True, pwd="", hint="") :
		asg = Assignments(name=name, courseid=cid, browsable=browsable, 
			passwordmessage=hint, password=pwd)
		return asg
		
class TaskViews() :
	def temp(request) :
		render_dict = {}
		return render(request, 'create-task.html', render_dict)

	def create(request):
		# if this is a POST request we need to process the form data
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = AssignmentForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				# process the data in form.cleaned_data as required
				# redirect to a new URL:
				return HttpResponseRedirect('/thanks/')
		# if a GET (or any other method) we'll create a blank form
		else:
			if request.session["stage"] == "details" :
				pass
			elif request.session["stage"] == "datetime" :
				form = AssignmentForm()
			formb = ReviewSettingsForm()
		return render(request, 'create-task.html', {'YaziForm': form, 'YaziFormzr': formb,})


	#@vary_on_cookie
	def upload(request, src, sname):
		dict_render['upload_url'] = '/avatar/%s/%s/' % (src, sname)
		if src == 'club' :
			real_name = ClubSnap.alias_find(sname)
			if real_name != sname and real_name :
				return HttpResponseRedirect('/avatar/club/%s/' % real_name)
		if request.method == 'POST':
			if 'image' in request.FILES :
				# This is an image submission
				img_file = request.FILES['image']
				temp_name = TaskBase.temp_name_get(img_file.name)
				temp_path = os.path.join(settings.MEDIA_ROOT, 'images', 'temp', temp_name)
				if img_file.size > 1800000:
					dict_render['content'] = 'This file is too large [core dumped]'
					return render(request, 'avatar_add.html', dict_render)
				try:
					file_token = open(temp_path, 'wb')
					logger.error('look at me ', temp_path)
					for chunk in img_file.chunks() :
						file_token.write(chunk)
					file_token.close()
				except Exception as e:
					import sys, traceback
					t,v,tb = sys.exc_info()
					logger.error('sth. went wrong... ')
					logger.error('e ' + str(e))
					logger.error('t ' + str(t))
					logger.error('v ' + str(v))
					dict_render['content'] = 'An error occured.'
					return render(request, 'avatar_add.html', dict_render)
				im = temp_path
				name = src + '-' + sname + ".png"
				return HttpResponseRedirect("/%s/%s/" % (src, sname))
				# What about other types?
			else :
				dict_render['content'] = 'Please choose a file'
				return render(request, 'avatar_add.html', dict_render)
		else:
			return render(request, 'avatar_add.html', dict_render)
