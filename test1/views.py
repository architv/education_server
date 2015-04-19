from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
import requests, json
import xml.etree.ElementTree as ET
import kookoo
from random import random, randint
from django.shortcuts import render, render_to_response

def call_ivr(request):
	if request.method == 'GET':
		print request.GET
		event = request.GET.get('event', None)
		print event
		if event == "GotDTMF":
			pincode = int(request.GET['data'])
			top_10_schools = SchoolNames.Query.all().limit(2)
			s = "The schools near you are "
			for school in top_10_schools:
				s += school.SCHOOL_NAME
				s += "  and"
			r = kookoo.Response()
			r.addPlayText(s)
			r.addHangup()
			return HttpResponse(r)
		else:
			r = kookoo.Response()
			pincode = r.append(kookoo.CollectDtmf(maxDigits=6))
			pincode.append(kookoo.PlayAudio("pincode.wav"))
			# pincode.append(kookoo.PlayText("Please enter the pincode"))
			return HttpResponse(r)

def get_coordinates(request):
	postal_code = request.GET.get('postal_code')
	geometry = requests.get("https://maps.googleapis.com/maps/api/geocode/json?components=postal_code:" + postal_code).json()["results"][0]["geometry"]
	coordinates = geometry["location"]
	return HttpResponse(json.dumps(coordinates))

def home(request):
	return render(request, "base.html")

def search(request):
	pass