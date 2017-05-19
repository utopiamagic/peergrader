from django.conf.urls import url

from .views import CourseViews

urlpatterns = [
	url(r'^create/$', CourseViews.create),
	url(r'^enroll/$', CourseViews.enroll),
	url(r'^([0-9]+)/$', CourseViews.view),
	url(r'^([0-9]+)/modify/$', CourseViews.modify),
	url(r'^([0-9]+)/members/$', CourseViews.members),
	url(r'^([0-9]+)/config/$', CourseViews.config),
	url(r'^all/$', CourseViews.list_specific),
	url(r'^list/$', CourseViews.list_brief),
	#url(r'^(\d)+/marking/$', CourseViews.listing),
]
