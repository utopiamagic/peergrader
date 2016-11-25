from django.conf.urls import url

from .views import AuthViews

urlpatterns = [
	url(r'^login/$', AuthViews.user_login),
	url(r'^signup/$', AuthViews.user_signup),
	url(r'^logout/$', AuthViews.user_logout),
]
