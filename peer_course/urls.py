from django.conf.urls import url

from .views import CourseViews

urlpatterns = [
	url(r'^create/$', CourseViews.create),
	url(r'^(\d)+/$', CourseViews.access),
	url(r'^all/$', CourseViews.listing),
]
