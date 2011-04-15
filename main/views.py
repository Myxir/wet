# Create your views here.
# -*- coding: utf-8 -*-

from django.http import HttpResponse
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
    template = loader.get_template('main/index.html')
    title = "Strona główna"
    context = Context({'title':title, 'STATIC_URL':settings.STATIC_URL, 'date':getDate()})
    return HttpResponse(template.render(context))

def vets(request):
    vetlist = Vet.objects.all().order_by('-pk')
    #all_clients = []
    #for vet in vetlist:
        #if not vet.client_set.all().isEmpty():
            
    template = loader.get_template('main/weterynarze.html')
    context = Context({'vetlist' : vetlist,})
    return HttpResponse(template.render(context))

def vet_details(request, vet_id):
    vet = Vet.objects.get(pk=vet_id)
    clientlist = vet.client_set.all()
    template = loader.get_template('main/weterynarze_details.html')
    context = Context({'clientlist': clientlist, 'vet':vet, 'len':len(clientlist)})
    return HttpResponse(template.render(context))

def client_details(request, client_id):
    client = Client.objects.get(pk=client_id)
    vet = client.vet
    animallist = client.animal_set.all()
    template = loader.get_template('main/klient_details.html')
    context = Context({'animallist': animallist, 'client':client, 'vet':vet})
    return HttpResponse(template.render(context))

def animal_details(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    client = animal.client
    vet = client.vet
    age = animal.age()
    template = loader.get_template('main/zwierzak_details.html')
    context = Context({'wiek':age, 'animal':animal, 'client':client, 'vet':vet})
    return HttpResponse(template.render(context));
    
    
