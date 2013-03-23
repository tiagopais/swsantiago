from django.contrib.auth.models import User
from django.db import models


class Auction(models.Model):
    user = models.ForeignKey(User)
    creation_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    auction_type = models.CharField(
        max_length=255,
        choices=(
            ('A', 'Apartment'),
            ('H', 'House'),
            ('R', 'Room'))
    )
    minimum_bid = models.DecimalField(max_digits=7, decimal_places=2)


class Bid(models.Model):
    user = models.ForeignKey(User)
    auction = models.ForeignKey(Auction)
    creation_date = models.DateField(auto_now_add=True)
    comment = models.TextField()
    value = models.DecimalField(max_digits=7, decimal_places=2)
