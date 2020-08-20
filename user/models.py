from django.db import models

class User(models.Model):
    first_name               = models.CharField(max_length = 64, null = False)
    last_name                = models.CharField(max_length = 64, null = False)
    email                    = models.EmailField(unique = True)
    phone                    = models.CharField(max_length = 64, null = False, unique = True)
    password                 = models.CharField(max_length = 128, null = False)
    birthdate                = models.DateField(null = True)
    is_newsletter_subscribed = models.BooleanField()
    is_top_contributor       = models.BooleanField()
