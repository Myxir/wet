from django.contrib import admin
from django.contrib.auth.models import User
from main.models import Vet
from main.models import Client
from main.models import Animal



class UserAdmin(admin.ModelAdmin):
	list_display = ('username','password','email','first_name','last_name','is_staff','is_active')

class ClientInline(admin.StackedInline): #to do js to collapse inline
    model = Client
    extra = 0
	
class VetAdmin(admin.ModelAdmin):
	list_display = ('__unicode__','showClients')
	inlines = [ClientInline]	

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Vet, VetAdmin)
admin.site.register(Client)
admin.site.register(Animal)
