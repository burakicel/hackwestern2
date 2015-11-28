from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Tutorial
from .models import User
from django.views.generic import TemplateView


 
def index(request):
	user_list = User.objects.all()
	tutorial_list = Tutorial.objects.order_by('created_at').reverse()
	output = dict()
	for i in range(0,5):
		output[str(i)+'_title'] = tutorial_list[i].tutorial_title
		output[str(i)+'_user'] = tutorial_list[i].user
		output[str(i)+'_repo_link'] = tutorial_list[i].repo_link
	context = RequestContext(request,output)
	template = loader.get_template('index.html')
	return HttpResponse(template.render(context))

