from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wet.views.home', name='home'),
    # url(r'^wet/', include('wet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'wet.main.views.index'),
    (r'^weterynarze/$', 'wet.main.views.vets'),
    (r'^weterynarze/(?P<vet_id>\d+)/$', 'wet.main.views.vet_details'),
    (r'^klienci/(?P<client_id>\d+)/$', 'wet.main.views.client_details'),
    (r'^zwierzaki/(?P<animal_id>\d+)/$', 'wet.main.views.animal_details'),
    (r'^login/$',  login, {'template_name': 'main/login.html'}),
    (r'^logout/$', logout, {'template_name': 'main/logout.html'}),
    
)

urlpatterns += staticfiles_urlpatterns() #development