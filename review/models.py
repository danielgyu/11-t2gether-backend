from django.db import models

class Review(models.Model):
    rating   = models.DecimalField(max_digits = 3, decimal_places = 2, null = False)
    product  = models.ForeignKey('product.Product', on_delete = models.CASCADE)
    reviewer = models.CharField(max_length = 100)
