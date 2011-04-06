
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
		return self.name + " " + self.surname + " (" + self.clinic_name + ")"; 
	
	def getClients(self):
		return self.client_set.get(pk=1)
	
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
		return self.name + " " + self.surname; 

class Animal(models.Model):
	
	client = models.ForeignKey(Client)
	species = models.CharField(max_length=120)
	race = models.CharField(max_length=120, blank = True)
	date_born = models.DateTimeField(blank = True)
	color = models.CharField(max_length=45, blank = True)
	photo = models.SlugField();
	history = models.TextField(blank = True)
	prognose = models.TextField(blank = True)
	added = models.DateTimeField(default = datetime.now(), editable = False)
	next_event = models.CharField(max_length=120, blank = True)
	next_event_date = models.DateTimeField(blank = True)
	
	def __unicode__(self):
		return self.species + " " + self.race; 