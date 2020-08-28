import json

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from elasticsearch_dsl.connections import connections

from main.models import MainImage

from .models      import Product, Size, Filter
from .documents   import ProductDocument


class AllTeaView(View):
    def get(self, request):
        styles = request.GET.getlist('style', None)
        types = request.GET.getlist('type', None)
        search_term  = request.GET.get('search', None)
        tea_products = Product.objects.prefetch_related('size_set', 'refine_set')

        if styles and types:
            tea_products = tea_products.filter(refine__name__in = styles).filter(refine__name__in = types)
        else:
            q = Q()
            if styles:
                q &= Q(refine__name__in = styles)
            if types:
                q &= Q(refine__name__in = types)
            tea_products = tea_products.filter(q)

        if search_term:
            search = ProductDocument.search().filter('match_phrase', main_name = search_term)
            search = [hit.main_name for hit in search]
            tea_products = tea_products.filter(main_name__in = search)

        tea_list = [{
            'product_id'    : product.id,
            'product_name'  : product.main_name,
            'product_price' : product.main_price,
            'product_image' : product.main_image,
            'size_unit'     : [tea.unit for tea in product.size_set.all()],
            'size_price'    : [tea.price for tea in product.size_set.all()],
            'size_image'    : [tea.image for tea in product.size_set.all()],
        } for product in tea_products]

        return JsonResponse({'product_list' : tea_list}, status = 200)

class RefineView(View):
    def get(self, request):
        data     = dict(request.GET.items())
        tea_products = Filter.objects.prefetch_related('product', 'refine')

        q = Q()
        if data:
            tea_products = \
                    list(tea_products.filter(refine__name__in = list(data.values()))\
                         .values('product__refine__name', 'product__refine__category').distinct())

        if not data:
            tea_products = list(tea_products.values('refine__category', 'refine__name').distinct())

        return JsonResponse({'product_list' : tea_products}, status = 200)

class TeaDetailView(View):
    def get(self, request, id):
        product = Product.objects.prefetch_related('size_set', 'information', 'image_set').get(id = id)
        brew_image = MainImage.objects.filter(numbering__in = [50, 51, 52])

        product_detail = {
            'product_type'     : product.classification.name,
            'product_name'     : product.main_name,
            'product_price'    : product.main_price,
            'product_image'    : list(product.image_set.values_list('url', flat = True)),
            'size_unit'        : list(product.size_set.values_list('unit', flat = True)),
            'size_price'       : list(product.size_set.values_list('price', flat = True)),
            'size_image'       : list(product.size_set.values_list('image', flat = True)),
            'description'      : product.information.description,
            'ingredients'      : product.information.ingredient,
            'brewing_quantity' : product.guide.quantity,
            'brewing_time'     : product.guide.time,
            'brewing_temp'     : product.guide.temperature,
            'quantity_img'    : brew_image.get(numbering = 50).info if product.guide.quantity else None,
            'time_img'         : brew_image.get(numbering = 51).info if product.guide.time else None,
            'temp_img'         : brew_image.get(numbering = 52).info if product.guide.temperature else None,
        }

        return JsonResponse({'product_detail' : product_detail}, status = 200)
