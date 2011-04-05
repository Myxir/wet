from django.contrib import admin
from main.models import Vet
from main.models import Client
from main.models import Animal

admin.site.register(Vet)
admin.site.register(Client)
admin.site.register(Animal)
