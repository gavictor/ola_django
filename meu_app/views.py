from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse

# Create your views here.
def index(request):
	template_name = 'index.html'
	
	return TemplateResponse(request, template_name, locals())