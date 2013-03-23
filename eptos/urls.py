from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
                       url(r'^$', 'commons.views.home', name='home'),
                       url(r'^login/$', login),
                       url(r'^logout/$', logout, {'next_page': reverse_lazy('common.views.home')})
                       # url(r'^eptos/', include('eptos.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
)
