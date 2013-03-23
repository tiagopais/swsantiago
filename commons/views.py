# Create your views here.
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import FormView, ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from commons.forms import CreateAuctionForm
from commons.models import Auction


def home(request):
    return render_to_response(
        'home.html',
        context_instance=RequestContext(request))


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


class AccountProfileView(TemplateView):
    template_name = 'account_profile.html'

    def get_context_data(self, **kwargs):
        context = super(AccountProfileView, self).get_context_data(**kwargs)

        context['user'] = self.request.user

        return context
