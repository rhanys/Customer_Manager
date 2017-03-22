from __future__ import unicode_literals

from django.db import models

class Customer(models.Model):
	name = models.CharField(max_length=100)
	nick = models.CharField(max_length=10)
	mail = models.CharField(max_length = 30)
	password = models.CharField(max_length = 16)
	def __unicode__(self):
		return self.name


# Create your models here.
