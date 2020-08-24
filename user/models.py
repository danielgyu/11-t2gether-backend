from django.db import models
from product.models import *

class User(models.Model):
    first_name               = models.CharField(max_length = 64, null = False)
    last_name                = models.CharField(max_length = 64, null = False)
    email                    = models.EmailField(unique = True)
    phone                    = models.CharField(max_length = 64, null = False, unique = True)
    password                 = models.CharField(max_length = 128, null = False)
    birthdate                = models.DateField(null = True)
    is_newsletter_subscribed = models.BooleanField()
    is_top_contributor       = models.BooleanField()
    wish_list                 = models.ManyToManyField(Product, through = 'Wishlist', related_name = 'wish')
    shopping_bag              = models.ManyToManyField(Product, through = 'ShoppingBag', related_name='shopping')

class Wishlist(models.Model):
    user_id    = models.ForeignKey(User, on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)

class ShoppingBag(models.Model):
    user_id   = models.ForeignKey(User, on_delete = models.CASCADE)
    procut_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    count     = models.IntegerField()
