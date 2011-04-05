# -*- coding: utf-8 -*-
from django.db import models

class Vet(models.Model):
	surname = models.CharField(max_length=120)	
	name = models.CharField(max_length=120)
	www = models.CharField(max_length=120)
	clinic_name = models.CharField(max_length=120)
	clinic_adress = models.CharField(max_length=120)
	phone = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	description = models.TextField()
	username = models.CharField(max_length=45)
	password = models.CharField(max_length=45)
	
class Client(models.Model):
	vet = models.ForeignKey(Vet)
	name = models.CharField(max_length=120)
	surname = models.CharField(max_length=120)
	phone = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	adress = models.CharField(max_length=120)
	username = models.CharField(max_length=45)
	password = models.CharField(max_length=45)	

class Animal(models.Model):
	client = models.ForeignKey(Client)
	species = models.CharField(max_length=120)
	race = models.CharField(max_length=120)
	date_born = models.DateTimeField()
	color = models.CharField(max_length=45)
	history = models.TextField()
	prognose = models.TextField()
	next_event = models.CharField(max_length=120)
	next_event_date = models.DateTimeField()
	
