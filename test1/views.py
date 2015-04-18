from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
import requests, json

def call_ivr(request):
	return HttpResponse("hello")

def get_coordinates(request):
	postal_code = request.GET.get('postal_code')
	geometry = requests.get("https://maps.googleapis.com/maps/api/geocode/json?components=postal_code:" + postal_code).json()["results"][0]["geometry"]
	coordinates = geometry["location"]
	return HttpResponse(json.dumps(coordinates))

def get_data(request):
	p = Post.objects.all()
	r = requests.get("https://google.com")
	return HttpResponse(str(p) + r.text) 

def add_data(request):
	p = Post()
	p.title = " jello"
	p.save()
	return HttpResponse("yo") 
# Create your views here.
