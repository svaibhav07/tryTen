from __future__ import unicode_literals
from django.conf import settings
from django.db import models


# Create your models here.
class profile(models.Model):
	name=models.CharField(max_length=120)
	user =models.OneToOneField(settings.AUTH_USER_MODEL, null=True,blank=True)
	description=models.TextField(default='description default text')# add blank=True,null=True to add no mandatory fields
	
	

	def __unicode__(self):
		return self.name

