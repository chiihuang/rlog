from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
	# /blog/
	url(r'^$', views.IndexView.as_view(), name='index'),
	# /polls/3/
	#url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	# /polls/3/results/
	#url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	# /polls3/vote/
	#url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)