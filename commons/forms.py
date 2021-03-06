from django import forms
from commons.models import Auction, Bid


class PlaceBidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['value']


class DetailAuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['name', 'address', 'auction_type', 'minimum_bid']


class CreateAuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['name', 'address', 'auction_type', 'minimum_bid']
