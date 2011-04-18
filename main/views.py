# -*- coding: utf-8 -*-
##TO DO: render_to_response('template.html', locals())!!!

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader
from main.models import Vet, Client, Animal
from wet import settings
from datetime import datetime

def getDate():
    a = str(datetime.today())[:11]
    txt = a[8:10]+"."
    txt += a[5:7]+"."
    txt += a[0:4]
    return txt

def index(request):
    title = "Strona główna"
    context = Context({'title':title, 'STATIC_URL':settings.STATIC_URL, 'date':getDate()})
    return render_to_response('main/index.html',context)

def vets(request):
    vetlist = Vet.objects.all().order_by('-pk')
    context = Context({'vetlist' : vetlist,})
    return render_to_response('main/weterynarze.html',context)

def vet_details(request, vet_id):
    vet = Vet.objects.get(pk=vet_id)
    clientlist = vet.client_set.all()
    context = Context({'clientlist': clientlist, 'vet':vet, 'len':len(clientlist)})
    return render_to_response('main/weterynarze_details.html',context)

def client_details(request, client_id):
    client = Client.objects.get(pk=client_id)
    vet = client.vet
    animallist = client.animal_set.all()
    context = Context({'animallist': animallist, 'client':client, 'vet':vet})
    return render_to_response('main/klient_details.html', context)

def animal_details(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    client = animal.client
    vet = client.vet
    age = animal.age()
    context = Context({'wiek':age, 'animal':animal, 'client':client, 'vet':vet})
    return render_to_response('main/zwierzak_details.html', context);
    
    
