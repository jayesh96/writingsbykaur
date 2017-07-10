from __future__ import unicode_literals

from django.db import models

# Create your models here.


from django.contrib.auth import get_user_model
User = get_user_model()

class Contact(models.Model):
	name = models.CharField(blank=False, null=False, max_length=200)
	email = models.EmailField(blank=False, null=False)
	subject = models.CharField(blank=False, null=False)
	message = models.TextField(blank=False, null=False)

	def __unicode__(self):
		return self.subject

	def __str__(self):
		return self.subject

