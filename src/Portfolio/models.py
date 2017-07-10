from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail

# Create your models here.




class Contact(models.Model):
	name = models.CharField(blank=False, null=False, max_length=200)
	email = models.EmailField(blank=False, null=False, max_length=200)
	subject = models.CharField(blank=False, null=False, max_length=200)
	message = models.TextField(blank=False, null=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.subject

	def __str__(self):
		return self.subject


def contact_post_saved_receiver(sender, instance, created, *args, **kwargs):
    obj = instance
    try:
    	email = 'jayesh.bidani@gmail.com'
    	subject = obj.subject
    	message = obj.message +'. This mail is sent by ' + obj.name + " " + obj.email
    	send_mail(subject, message, email, email)
    	print(subject, message)

    except:
    	pass

post_save.connect(contact_post_saved_receiver, sender=Contact)
