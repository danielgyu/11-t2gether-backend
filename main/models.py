from django.db import models

class MainImage(models.Model):
    purpose    = models.CharField(max_length = 64, null = False)
    numbering  = models.IntegerField()
    info       = models.CharField(max_length = 2048, null = False)
