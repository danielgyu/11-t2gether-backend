import csv, re
from product.models import (MainCategory,
                            SubCategory,
                            Type,
                            Guide,
                            Product,
                            Refine,
                            Information,
                            Size,
                            Filter,
                            Image)


style_list = ['loose leaf tea', 'loose leaf tisane', 'powdered tisane', 'sugar', 'teabag']
type_list = ['black breakfast tea', 'black tea', 'chinese black tea', 'chinese green tea',
             'flavoured black tea', 'flavoured green tea', 'flavoured oolong tea',
             'flavoured white tea', 'fruit tisane', 'herbal tisane', 'japanese green tea',
             'oolong tea', 'premium green tea', 'smoked black tea', 'white tea']

style_loose_path = 'scripts/style_LooseLeafTea.csv'
style_sugar = 'scripts/style_Sugar.csv'
type_BBT = 'scripts/type_BlackBreakfastTea.csv'
type_CGT = 'scripts/type_ChineseGreenTea.csv'
type_FOT = 'scripts/type_FlavoredOolongTea.csv'
total_path = [style_loose_path, style_sugar, type_BBT, type_CGT, type_FOT]


for style in style_list:
    Refine.objects.get_or_create(name = style, category = 1)

for tea_type in type_list:
    Refine.objects.get_or_create(name = tea_type, category = 2)
# Refin1 = Style, Refine2 = Type of Tea

def run():

    # Type.objects.get_or_create(name = 'other', sub_category = SubCategory.objects.get(id = 1))

    file = open(type_FOT)
    reader = csv.reader(file)
    next(reader)

    for row in reader:

        Guide.objects.get_or_create(quantity = row[4],
                                time = row[5],
                                temperature = row[6])
        main_price = None
        if row[13]:
            main_price = re.findall('\d+\.\d+', row[13])[0]
        if Product.objects.filter(main_name = row[1]).exists():
            pass
        else:
            Product.objects.get_or_create(classification = Type.objects.get(name = 'other'),
                                   guide = Guide.objects.get(quantity = row[4],
                                                             time = row[5],
                                                             temperature = row[6]),
                                   main_name = row[1],
                                   main_image = row[2],
                                   main_price = main_price,
                                   product_name = row[3],
                                   stock = 100)

            Information.objects.get_or_create(product = Product.objects.get(main_name = row[1]),
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
                    Size.objects.get_or_create(product = Product.objects.get(main_name = row[1]),
                                        unit = u,
                                        price = p,
                                        image = i)

            to_lst = row[10].split(',')
            for image in to_lst:
                image = re.findall('https.*[fit]', image)[0]
                Image.objects.get_or_create(product = Product.objects.get(main_name = row[1]),
                                     url = image)

        Filter.objects.get_or_create(product = Product.objects.get(main_name = row[1]),
                                     refine = Refine.objects.get(name = 'flavoured oolong tea'))
