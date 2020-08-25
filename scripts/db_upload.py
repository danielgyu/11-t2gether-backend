import csv, re

from product.models import (MainCategory,
                            SubCategory,
                            Type,
                            Guide,
                            Product,
                            Refine,
                            Information,
                            Size,
                            Image)

path = 'scripts/t2.csv'

def run():
    file = open(path)
    reader = csv.reader(file)
    next(reader)

    Type.objects.all().delete()
    Guide.objects.all().delete()
    Product.objects.all().delete()
    Information.objects.all().delete()
    Size.objects.all().delete()
    Image.objects.all().delete()

    sub = SubCategory.objects.get(id = 1)
    for row in reader:
        Type.objects.get_or_create(name = row[0], sub_category = sub)

        Guide.objects.get_or_create(quantity = row[4],
                                   time = row[5],
                                   temperature = row[6])

        main_price = None
        if row[13]:
            main_price = re.findall('\d+\.\d+', row[13])[0]
        Product.objects.create(classification = Type.objects.get(name = row[0]),
                               guide = Guide.objects.get(quantity = row[4],
                                                         time = row[5],
                                                         temperature = row[6]),
                               main_name = row[1],
                               main_image = row[2],
                               main_price = main_price,
                               product_name = row[3],
                               stock = 100)

        Information.objects.create(product = Product.objects.get(main_name = row[1]),
                                   description = row[11],
                                   ingredient = row[12])

        size_u = size_p = size_i = None
        row[7] = row[7].replace('[]', '')
        row[8] = row[8].replace('[]', '')
        row[9] = row[9].replace('[]', '')
        if row[7] and row[8] and row[9]:
            size_u = row[8].split(',')
            size_p = row[9].split(',')
            size_i = row[7].split(',')
            for u, p, i in zip(size_u, size_p, size_i):
                u = re.findall('([A-Za-z0-9\-\_\.\ ]+)', u.strip())[0]
                p = re.findall('\d+\.\d+', p)[0]
                i = re.findall('https.*[fit]', i)[0]
                Size.objects.create(product = Product.objects.get(main_name = row[1]),
                                    unit = u,
                                    price = p,
                                    image = i)

        to_lst = row[10].split(',')
        for image in to_lst:
            image = re.findall('https.*[fit]', image)[0]
            Image.objects.create(product = Product.objects.get(main_name = row[1]),
                                 url = image)
