from django.db import models

# Create your models here.
class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	tit = models.CharField(max_length=255)

	def __unicode__(self):
		return self.tit