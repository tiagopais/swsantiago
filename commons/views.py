# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import FormView
from commons.forms import CreateAuctionForm


def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


@login_required
def auction_detail(request, auction_id):

    return render_to_response('auction_detail.html', context_instance=RequestContext(request))


class CreateAuctionView(FormView):
    template_name = 'auction_create.html'
    form_class = CreateAuctionForm

    def form_valid(self, form):
        auction = form.instance

        auction.user = self.request.user
        auction.save()

        return HttpResponseRedirect(reverse_lazy(auction_detail, args=(auction.id,)))