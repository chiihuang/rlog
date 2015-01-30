from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
	template_name = 'blog/index.html'
	#context = {}
	#context_object_name = 'latest_question_list'
	#return render(request, 'blog/index.html', context)