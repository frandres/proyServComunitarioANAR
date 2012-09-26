from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anar.views.home', name='home'),
    # url(r'^anar/', include('anar.foo.urls')),
    url(r'^yacimientos/$', 'anarapp.views.index'),
    url(r'^mapa/$', 'geoespacial.views.mapa'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
