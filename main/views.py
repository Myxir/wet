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
    vetlist = Vet.objects.all().order_by('-added')
    #all_clients = []
    #for vet in vetlist:
        #if not vet.client_set.all().isEmpty():
            
    template = loader.get_template('main/weterynarze.html')
    context = Context({'vetlist' : vetlist,})
    return HttpResponse(template.render(context))

def vet_details(request, vet_id):
    vet = Vet.objects.get(pk=vet_id)
    return HttpResponse(u"Strona pojedynczego weterynarza o id %s:\
     wszyscy jego klienci i podopieczni." %vet_id + "<br><br>" + vet.username)

def client_details(request, client_id):
    client = Client.objects.get(pk=client_id)
    
    return HttpResponse(u"Strona pojedynczego klienta  od id %s \
    wraz z jego zwierzakami. odnośniki do lekarza i zwierzaków." %client_id + "<br><br>" + client.username)

def animal_details(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return HttpResponse(u"Strona ze szczegółami zwierzaka od id %s, \
    link do jego pana i lekarza." %animal_id + "<br><br>" + animal.species +" "+animal.race)