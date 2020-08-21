from django.db import models

class MainCategory(models.Model):
    name = models.CharField(max_length = 40)

class SubCategory(models.Model):
    name = models.CharField(max_length = 40)
    main_category = models.ForeignKey(MainCategory, on_delete = models.CASCADE)

class Type(models.Model):
    name = models.CharField(max_length = 100)
    sub_category = models.ForeignKey(SubCategory, on_delete = models.CASCADE)

class Guide(models.Model):
    quantity = models.CharField(max_length = 100, null = True)
    time = models.CharField(max_length = 40, null = True)
    temperature = models.CharField(max_length = 40, null = True)

class Product(models.Model):
    classification = models.ForeignKey(Type, on_delete = models.CASCADE)
    guide = models.ForeignKey(Guide, on_delete = models.CASCADE)
    main_name = models.CharField(max_length = 100)
    main_image = models.URLField()
    main_price = models.DecimalField(max_digits = 6, decimal_places = 2, null = True)
    product_name = models.CharField(max_length = 100)
    stock = models.IntegerField()

class Refine(models.Model):
    name = models.CharField(max_length = 100)
    category = models.PositiveSmallIntegerField()
    product = models.ManyToManyField(Product)

class Information(models.Model):
    product = models.OneToOneField(Product, on_delete = models.CASCADE)
    description = models.CharField(max_length = 300)
    ingredient = models.CharField(max_length = 200)

class Size(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    unit = models.CharField(max_length = 100, null = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2, null = True)
    image = models.URLField(null = True)

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    url = models.URLField()
