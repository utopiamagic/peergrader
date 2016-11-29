from django.shortcuts import render
from .models import *

# Create your views here.

class CourseBase :
	def all() :
		result = CourseList.objects.all()
		return result
		
class CourseViews :
	def create() :
		pass
