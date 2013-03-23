from django import forms
from commons.models import Auction


class CreateAuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['name', 'address', 'auction_type', 'minimum_bid']