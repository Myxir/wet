
from django.db import models
from datetime import datetime

class Vet(models.Model):
	
	surname = models.CharField(max_length=120)	
	name = models.CharField(max_length=120)
	www = models.URLField(blank = True)
	email = models.EmailField(max_length=45)
	clinic_name = models.CharField(max_length=120)
	clinic_adress = models.CharField(max_length=120)
	phone = models.CharField(max_length=45)
	description = models.TextField(blank = True)
	added = models.DateTimeField(default = datetime.now(), editable = False)
	username = models.CharField(max_length=45, unique=True)
	password = models.CharField(max_length=45)
	
	def __unicode__(self):
		return self.name + " " + self.surname + " (" + self.username + ")"
	
	def showClients(self):
		return self.client_set.all()

	
class Client(models.Model):
	
	vet = models.ForeignKey(Vet)
	name = models.CharField(max_length=120)
	surname = models.CharField(max_length=120)
	phone = models.CharField(max_length=45, blank = True)
	email = models.EmailField(max_length=45, blank = True)
	adress = models.CharField(max_length=120, blank = True)
	added = models.DateTimeField(default = datetime.now(), editable = False)
	username = models.CharField(max_length=45, unique=True)
	password = models.CharField(max_length=45)	
	
	def __unicode__(self):
		return self.name + " " + self.surname + " (" + self.username + ")"

class Animal(models.Model):
	
	client = models.ForeignKey(Client)
	species = models.CharField(max_length=120)
	race = models.CharField(max_length=120, blank = True)
	date_born = models.DateField(blank = True, null=True)
	color = models.CharField(max_length=45, blank = True)
	photo = models.SlugField(blank = True);
	history = models.TextField(blank = True)
	prognose = models.TextField(blank = True)
	added = models.DateTimeField(default = datetime.now(), editable = False)
	next_event = models.CharField(max_length=120, blank = True)
	next_event_date = models.DateTimeField(blank = True, null=True)
	
	def __unicode__(self):
		return self.species + " " + self.race; 