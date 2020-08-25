import json

from django.views import View
from django.http  import JsonResponse

from .models      import Product, Size, Filter

class AllTeaView(View):
    def get(self, request):
        tea_products = Product.objects.prefetch_related('size_set')

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

class RefineView(View):
    def post(self, request):
        styles   = request.GET.getlist('style', None)
        teas     = request.GET.getlist('type', None)
        all_teas = Product.objects.prefetch_related('filter_set', 'refine_set', 'size_set')
        refines = products = filters = None

        if styles and not teas:
            for style in styles:
                products = [tea for tea in all_teas.filter(refine__name = style)]

        elif teas and not styles:
            for tea in teas:
                products = [tea for tea in all_teas.filter(refine__name = tea)]

        else:
            refines = styles + teas
            for refine in refines:
                all_teas = all_teas.filter(refine__name = refine)
            products = [product for product in all_teas]

        filters  = Filter.objects.filter(product__main_name__in=[product.main_name for product in products])

        tea_list = [{
            'product_id'    : product.id,
            'product_name'  : product.main_name,
            'product_price' : product.main_price,
            'product_image' : product.main_image,
            'size_unit'     : [tea.unit for tea in product.size_set.all()],
            'size_price'    : [tea.unit for tea in product.size_set.all()],
            'size_image'    : [tea.unit for tea in product.size_set.all()],
            'refine'        : list(filters.values_list('refine__category', 'refine__name').distinct()),
        } for product in products]

        return JsonResponse({'product_list' : tea_list}, status = 200)
