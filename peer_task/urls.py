from django.conf.urls import url

from .views import TaskViews

urlpatterns = [
	url(r'^create/$', TaskViews.create),
	#url(r'^(\d)+/$', TaskViews.access),
	#url(r'^(\d)+/modify/$', TaskViews.modify),
	#url(r'^all/$', TaskViews.listing),
]
