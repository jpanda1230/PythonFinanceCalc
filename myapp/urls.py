# howdy/urls.py
from django.conf.urls import url
from myapp import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^output/$', views.AboutPageView.as_view()), # Add this /about/ route
	url(r'^forward/$', views.ForwardPageView.as_view()),
]