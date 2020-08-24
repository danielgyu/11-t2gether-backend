from django.db import models
from product.models import Product

class User(models.Model):
    first_name               = models.CharField(max_length = 64, null = False)
    last_name                = models.CharField(max_length = 64, null = False)
    email                    = models.EmailField(unique = True)
    phone                    = models.CharField(max_length = 64, null = False, unique = True)
    password                 = models.CharField(max_length = 128, null = False)
    birthdate                = models.DateField(null = True)
    is_newsletter_subscribed = models.BooleanField()
    is_top_contributor       = models.BooleanField()
    wishlist                 = models.ManyToManyField('Product', thourgh = 'Wishlist')
    shoppingbag              = models.ManyToManyField('Product', through = 'ShoppingBag')

class Wishlist(models.Model):
    user_id    = models.ForeignKey('User', on_delete = models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete = models.CASCADE)

class ShoppingBag(models.Model):
    user_id   = models.ForeignKey('User', on_delete = models.CASCADE)
    procut_id = models.ForeignKey('Product', on_delete)
    count     = models.IntegerField()
