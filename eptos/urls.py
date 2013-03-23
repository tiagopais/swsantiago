from django.conf.urls import patterns, include, url

from django.contrib import admin
from registration.views import register

admin.autodiscover()
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy
from commons.views import CreateAuctionView, auction_detail

urlpatterns = patterns(
    '',
    url(r'^accounts/register/$',
        register,
        {
            'backend': 'registration.backends.simple.SimpleBackend',
            'success_url': reverse_lazy('commons.views.home')
        },
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^$', 'commons.views.home', name='home'),
    url(r'^login/$', login),
    url(r'^logout/$', logout, {'next_page': reverse_lazy('commons.views.home')}, name='logout'),

    url(r'^auctions/(?P<auction_id>\d+)/$', auction_detail),
    url(r'^auctions/create/$', login_required(CreateAuctionView.as_view())),
    # url(r'^eptos/', include('eptos.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    )
