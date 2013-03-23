# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import FormView, ListView
from django.template import RequestContext
from commons.forms import CreateAuctionForm
from commons.models import Auction


def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


class CreateAuctionView(FormView):
    template_name = 'auction_create.html'
    form_class = CreateAuctionForm

    def form_valid(self, form):
        auction = form.instance

        auction.user = self.request.user
        auction.save()

        return super(CreateAuctionView, self).form_valid(form)


class AuctionListView(ListView):
    model = Auction
    template_name = 'auction_list.html'
