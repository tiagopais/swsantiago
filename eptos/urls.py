from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy
from commons.views import CreateAuctionView

urlpatterns = patterns(
    '',
    url(r'^$', 'commons.views.home', name='home'),
    url(r'^login/$', login),
    url(r'^logout/$', logout, {'next_page': reverse_lazy('commons.views.home')}, name='logout'),
    url(r'^auctions/create/$', login_required(CreateAuctionView.as_view())),
    # url(r'^eptos/', include('eptos.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
