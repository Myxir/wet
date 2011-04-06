from django.contrib import admin
from main.models import Vet
from main.models import Client
from main.models import Animal

class ClientInline(admin.StackedInline): #to do js to collapse inline
    model = Client
    extra = 0

class AdminVet(admin.ModelAdmin):
    fields = ['username', 'password', 'surname', 'name', 'clinic_name', \
              'clinic_adress', 'phone', 'email', 'www', 'description']
    inlines = [ClientInline]
    
class AdminClient(admin.ModelAdmin):
    fields = ['username', 'password', 'vet_id', 'name', 'surname', 'phone', 'email', 'adress']
        
admin.site.register(Vet, AdminVet)
admin.site.register(Client)
admin.site.register(Animal)
