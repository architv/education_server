from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
import requests, json
import xml.etree.ElementTree as ET
import kookoo
import logging

def call_ivr(request):
	if request.method == 'GET':
		print request.GET
		event = request.GET.get('event', None)
		print event
		logger = logging.getLogger('testlogger')
		logger.info(event)
		if event == "GotDTMF":
			pincode = int(request.GET['data'])
			top_10_schools = SchoolNames.Query.all().limit(10)
			s = ""
			for school in top_10_schools:
				s += school.SCHOOL_NAME
			r = kookoo.Response()
			r.addPlayText(s)
			return HttpResponse(r)
		else:
			r = kookoo.Response()
			pincode = r.append(kookoo.CollectDtmf(maxDigits=6))
			pincode.append(kookoo.PlayText("Please enter the input"))
			return HttpResponse(r)
		return HttpResponse("error")

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
