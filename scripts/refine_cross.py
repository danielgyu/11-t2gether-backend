from product.models import *

def run():
    products = ['Morning Sunshine Loose Leaf Tea',
                'English Breakfast Loose Leaf Tea',
                'Irish Breakfast Loose Leaf Tea',
                'Organic Pekoe Loose Leaf Tea',
                'Ausssie Wattle Breakfast Loose Leaf Tea',
                'Good Morning Loose Leaf Tea']

    products2 = ['China Jasmine Loose Leaf Tea',
                 'Gunpowder Green Loose Leaf Tea',
                 'Chinese Sencha Loose Leaf Tea']

    products3 = ['Oolong Chocolate Chai Loose Leaf Tea',
                 'Oolong Fresh Loose Leaf Gift Cube',
                 'Toasty Warm Loose Leaf Gift Cube']

    r1 = Refine.objects.get(name = 'loose leaf tea')
    r2 = Refine.objects.get(name = 'black breakfast tea')
    r3 = Refine.objects.get(name = 'chinese green tea')
    r4 = Refine.objects.get(name = 'flavoured oolong tea')

    for product in products:
        if Product.objects.get(main_name = product).exists():
            p = Product.objects.get(main_name = product)
            Filter.objects.get_or_create(product = p,
                                         refine = r1)
            Filter.objects.get_or_create(product = p,
                                         refine = r2)
    for product in products2:
        if Product.objects.get(main_name = product).exists():
            p = Product.objects.get(main_name = product)
            Filter.objects.get_or_create(product = p,
                                        refine = r1)
            Filter.objects.get_or_create(product = p,
                                        refine = r3)

    for product in products3:
        if Product.objects.get(main_name = product).exists():
            p = Product.objects.get(main_name = product)
            Filter.objects.get_or_create(product = p,
                                        refine = r1)
            Filter.objects.get_or_create(product = p,
                                        refine = r4)
