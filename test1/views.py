from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

def get_data(request):
	p = Post.objects.all()
	return HttpResponse(p) 

def add_data(request):
	p = Post()
	p.tit = " jello"
	p.save()
	return HttpResponse("yo") 
# Create your views here.
