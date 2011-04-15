
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Vet(models.Model):
	user = models.OneToOneField(User)
	www = models.URLField(blank = True)
	clinic_name = models.CharField(max_length=120)
	clinic_adress = models.CharField(max_length=120, blank = False)
	clinic_city = models.CharField(max_length=45, blank = False)
	phone = models.CharField(max_length=45, blank = True)
	
	def showClients(self):
		return self.client_set.all()
	def __unicode__(self):
		if(len(self.clinic_name)==0):
			txt = self.user.first_name + " " +self.user.last_name
		else:
			txt = self.user.first_name + " " +self.user.last_name + " ("+self.clinic_name+")" 
		return txt

	
class Client(models.Model):
	user = models.OneToOneField(User)
	vet = models.ForeignKey(Vet)
	phone = models.CharField(max_length=45, blank = True)
	adress = models.CharField(max_length=120, blank = True)
	
	def __unicode__(self):
		return self.user.first_name +" " +self.user.last_name

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
	def age(self):
		return datetime.today() #to do date calculation
