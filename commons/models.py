from django.contrib.auth.models import User
from django.db import models


class Auction(models.Model):
    user = models.ForeignKey(User)
    creation_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=255, verbose_name='Where is it?')
    name = models.CharField(max_length=255, verbose_name='Pick an original name for your offering')
    auction_type = models.CharField(
        max_length=255,
        verbose_name='What type of type of place is it?',
        choices=(
            ('A', 'Apartment'),
            ('H', 'House'),
            ('R', 'Room'))
    )
    minimum_bid = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='How much are you asking for?')


class Bid(models.Model):
    user = models.ForeignKey(User)
    auction = models.ForeignKey(Auction)
    creation_date = models.DateField(auto_now_add=True)
    comment = models.TextField()
    value = models.DecimalField(max_digits=7, decimal_places=2)
