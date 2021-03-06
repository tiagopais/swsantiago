# -*- coding: utf-8 -*-

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import FormView, ListView
from django.views.generic import DetailView, TemplateView
from django.template import RequestContext
from commons.forms import CreateAuctionForm, PlaceBidForm
from commons.models import Auction


def home(request):

    auctions = Auction.objects.all()

    return render_to_response(
        'home.html',
        {
            'auctions': auctions
        },
        context_instance=RequestContext(request))


def auction_detail(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)

    return render_to_response('auction_detail.html',
                              {
                                  'auction': auction,
                                  'bid_form': PlaceBidForm()
                              },
                              context_instance=RequestContext(request))


@login_required
def place_bid(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)

    if request.method == 'POST':

        form = PlaceBidForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.auction = auction
            form.save()

            request.flash['success'] = u'Bid placed successfully for %s!' % form.instance.value
        else:
            return render_to_response('auction_detail.html',
                                      {
                                          'auction': auction,
                                          'bid_form': form
                                      },
                                      context_instance=RequestContext(request))

    return HttpResponseRedirect(reverse_lazy(auction_detail, args=(auction.id,)))


class AuctionDetailView(DetailView):
    model = Auction
    template_name = 'auction_detail.html'


class CreateAuctionView(FormView):
    template_name = 'auction_create.html'
    form_class = CreateAuctionForm

    def form_valid(self, form):
        auction = form.instance
        auction.user = self.request.user
        auction.save()

        self.request.flash['success'] = 'Auction created successfully!'

        return HttpResponseRedirect(
            reverse_lazy('auction_detail', args=(auction.id,)))


class AuctionListView(ListView):
    model = Auction
    template_name = 'auction_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'detail_user'


class AccountProfileView(TemplateView):
    template_name = 'account_profile.html'

    def get_context_data(self, **kwargs):
        context = super(AccountProfileView, self).get_context_data(**kwargs)

        context['user'] = self.request.user

        return context
