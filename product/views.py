from django.views            import View
from django.http             import JsonResponse

from .models     import Product, Size


class AllTeaView(View):
    @query_debugger
    def get(self, request):
        tea_products = Product.objects.prefetch_related('size_set')

        tea_list = [{
            'product_id' : product.id,
            'product_name' : product.main_name,
            'product_price' : product.main_price,
            'product_image' : product.main_image,
            'size_unit' : [tea.unit for tea in product.size_set.all()],
            'size_price' : [tea.price for tea in product.size_set.all()],
            'size_image' : [tea.image for tea in product.size_set.all()],
        } for product in tea_products]

        return JsonResponse({'product_list' : tea_list[:30]}, status = 200)
