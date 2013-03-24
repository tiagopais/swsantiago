from django.conf.urls import patterns, include, url

from django.contrib import admin
from registration.views import register

admin.autodiscover()
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy
from commons.views import CreateAuctionView, AuctionListView, auction_detail, place_bid, UserDetailView, AccountProfileView

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
    url(r'^logout/$',
        logout, {'next_page': reverse_lazy('commons.views.home')},
        name='logout'),

    url(r'^auctions/(?P<auction_id>\d+)/$',
        auction_detail,
        name='auction_detail'),
    url(r'^auctions/(?P<auction_id>\d+)/place_bid$',
        place_bid,
        name='place_bid'),
    url(r'^auctions/create/$',
        login_required(CreateAuctionView.as_view()),
        name='create_auction'),
    url(r'^auctions/$', AuctionListView.as_view(),
        name='auctions_list'),
    url(r'^accounts/profile/$',
        AccountProfileView.as_view(),
        name='user_profile'),
    url(r'^users/(?P<pk>\d+)/$',
        UserDetailView.as_view(),
        name='user_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
