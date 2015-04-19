from django.db import models
from parse_rest.connection import register
from parse_rest.datatypes import Object, GeoPoint
from parse_rest.user import User
import json, requests

register('P3N8sjOcUB7pMF3G1miWIfswdXGx6MN2MzBJ8I3M', 'EGxO4lNrnlbYcDz6h36vAFLDTMiLG4tSVyU2RRE0')

# Create your models here.
class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)

	def __unicode__(self):
		return self.title

class SchoolNames(Object):
	pass