import json

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from .models      import Product, Size, Filter


class AllTeaView(View):
    def get(self, request):
        styles = request.GET.getlist('style', None)
        types = request.GET.getlist('type', None)
        tea_products = Product.objects.prefetch_related('size_set', 'refine_set')

        if styles and types:
            tea_products = Product.objects.filter(refine__name__in = styles).filter(refine__name__in = types)
        else:
            q = Q()
            if styles:
                q &= Q(refine__name__in = styles)
            if types:
                q &= Q(refine__name__in = types)
            tea_products = tea_products.filter(q)

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
        styles   = request.GET.getlist('style', None)
        teas     = request.GET.getlist('type', None)
        tea_products = []

        if styles:
            tea_products += list(Filter.objects.filter(
                refine__name__in = styles).values(
                    'product__refine__name', 'product__refine__category').distinct())
        if teas:
            tea_products += list(Filter.objects.filter(
                refine__name__in = teas).values(
                    'product__refine__name', 'product__refine__category').distinct())
        if not styles and not teas:
            tea_products = list(Filter.objects.values('refine__category', 'refine__name').distinct())

        return JsonResponse({'product_list' : tea_products}, status = 200)

class TeaDetailView(View):
    def get(self, request, id):
        product = Product.objects.prefetch_related('size_set', 'information').get(id = id)

        product_detail = [{
            'product_type'     : product.classification.name,
            'product_name'     : product.main_name,
            'product_price'    : product.main_price,
            'product_image'    : product.main_image,
            'size_unit'        : list(product.size_set.values_list('unit', flat = True)),
            'size_price'       : list(product.size_set.values_list('price', flat = True)),
            'size_image'       : list(product.size_set.values_list('image', flat = True)),
            'description'      : product.information.description,
            'ingredients'      : product.information.ingredient,
            'brewing_quantity' : product.guide.quantity,
            'brewing_time'     : product.guide.time,
            'brewing_temp'     : product.guide.temperature,
        }]

        return JsonResponse({'product_detail' : product_detail}, status = 200)

