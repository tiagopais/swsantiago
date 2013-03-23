from django.contrib.auth.models import User
from django.db import models
from django.template import Context
from django.template.loader import get_template
from django.utils.safestring import mark_safe


class Auction(models.Model):
    user = models.ForeignKey(User)
    creation_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=255, verbose_name='Where is it?')
    name = models.CharField(
        max_length=255,
        verbose_name='Pick an original name for your offering')

    AUCTION_TYPE_CHOICES = (
        ('A', 'Apartment'),
        ('H', 'House'),
        ('R', 'Room'))
    auction_type = models.CharField(
        max_length=255,
        verbose_name='What type of type of place is it?',
        choices=AUCTION_TYPE_CHOICES
    )
    minimum_bid = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='How much are you asking for?')

    def list_display(self):
        t = get_template('auctions/list_display.html')
        c = Context({'auction': self})
        return mark_safe(t.render(c))

    def pretty_auction_type(self):
        return dict(Auction.AUCTION_TYPE_CHOICES)[self.auction_type]

    def pretty_minimum_bid(self):
        return u'US$ {0}'.format(self.minimum_bid)


class Bid(models.Model):
    user = models.ForeignKey(User)
    auction = models.ForeignKey(Auction)
    creation_date = models.DateField(auto_now_add=True)
    comment = models.TextField()
    value = models.DecimalField(max_digits=7, decimal_places=2)
