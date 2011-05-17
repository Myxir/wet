# -*- coding: utf-8 -*-
##TO DO: render_to_response('template.html', locals())!!!

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader
from main.models import Vet, Client, Animal
from wet import settings
from datetime import datetime
from django.http  import Http404
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def auth(request): http://stackoverflow.com/questions/3463240/check-if-onetoonefield-is-none-in-django
    if(request.user.is_authenticated()):
        user = request.user
        if(user.vet)
        txt = "zalogowano jako: </br>" + "<a id=\"light\" href=/weterynarze/"+str(user.pk)+">"+user.username +"</a>"+\
        "</br><a id=\"light\" href=/logout>wyloguj</a>"
    else:
        txt = "<a id=\"light\" href=/login>zaloguj / zarejestruj</a>"
    return txt

def getDate():
    a = str(datetime.today())[:11]
    txt = a[8:10]+"."
    txt += a[5:7]+"."
    txt += a[0:4]
    return txt

def index(request):
    txt = auth(request)
    context = Context({'STATIC_URL':settings.STATIC_URL, 'date':getDate(), 'logged':txt})
    return render_to_response('main/index.html',context)

def vets(request):
    vetlist = Vet.objects.all().order_by('-pk')
    
    txt = auth(request)    
    paginator = Paginator(vetlist, 10) # Show 25 contacts per page
    
    page = request.GET.get('page')
    try:
        vetpag = paginator.page(page)
    except TypeError:
        vetpag = paginator.page(1)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        vetpag = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        vetpag = paginator.page(paginator.num_pages)

        
    context = Context({'vetlist' : vetlist, "log":txt, 'STATIC_URL':settings.STATIC_URL, 'date':getDate(), 'logged':txt, 'vetpag':vetpag})
    return render_to_response('main/weterynarze.html',context)

def vet_details(request, vet_id):
    try:
        vet = Vet.objects.get(pk=vet_id)
    except Vet.DoesNotExist:
        raise Http404
    
    txt = auth(request)
    
    clientlist = vet.client_set.all()
    if not (request.user.is_authenticated and \
    (request.user.username == vet.user.username or request.user.is_staff)):
        clientlist = 'false'
    context = Context({'clientlist': clientlist, 'vet':vet, 'len':len(clientlist),'STATIC_URL':settings.STATIC_URL, 'date':getDate(), 'logged':txt})
    return render_to_response('main/weterynarze_details.html',context)
    
def client_details(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        raise Http404
    txt = auth(request)
    if not (request.user.is_authenticated and \
    (request.user.username == client.user.username \
     or request.user.username == client.vet.user.username or request.user.is_staff)):
        vet = 'false'
        animallist = []
    else:
        vet = client.vet
        animallist = client.animal_set.all()
    context = Context({'animallist': animallist, 'client':client, 'vet':vet,'STATIC_URL':settings.STATIC_URL, 'date':getDate(), 'logged':txt})
    return render_to_response('main/klient_details.html', context)

def animal_details(request, animal_id):
    try:
        animal = Animal.objects.get(pk=animal_id)
    except Animal.DoesNotExist:
        raise Http404
    txt = auth(request)
    if not (request.user.is_authenticated and \
    (request.user.username == animal.client.user.username \
     or request.user.username == animal.client.vet.user.username or request.user.is_staff)):
        client = 'false'
        vet = 'false'
        age = 'false'
    else:
        client = animal.client
        vet = client.vet
        age = animal.age()
    context = Context({'wiek':age, 'animal':animal, 'client':client, 'vet':vet,'STATIC_URL':settings.STATIC_URL, 'date':getDate(), 'logged':txt})
    return render_to_response('main/zwierzak_details.html', context);

    
