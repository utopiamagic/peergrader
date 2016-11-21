from django.conf.urls import url

from .views import AuthViews

urlpatterns = [
	url(r'^login/$', AuthViews.main),
	url(r'^signup/$', AuthViews.main),
]
