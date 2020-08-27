from django.shortcuts import render
from django.views     import View
from django.http      import JsonResponse
from django.db.models import Avg, Count

from main.models      import MainImage

from .models          import Review

class ReviewView(View):
    def get(self, request):
        star = MainImage.objects.filter(numbering__in = [60, 61, 62])
        review_list = [{
            'product_id'   : review.get('product'),
            'rating'       : float(review.get('rate_avg')),
            'rating_img'   : star.get(purpose = 'five star').info \
            if float(review.get('rate_avg')) > 4.3  else star.get(purpose = 'four star').info \
            if float(review.get('rate_avg')) < 3.5  else star.get(purpose = 'three star').info,
            'review_count' : review.get('review_count'),
        } for review in Review.objects.values('product').annotate(rate_avg = Avg('rating')
                                                                 ).annotate(review_count = Count('product'))]
        return JsonResponse({'review_list' : review_list}, status = 200)

class ReviewDetailView(View):
    def get(self, request, id):
        star   = MainImage.objects.filter(numbering__in = [60, 61, 62])
        review = Review.objects.values('product').annotate(rate_avg = Avg('rating')
                                                          ).annotate(review_count = Count('product')
                                                                    ).get(product__id = id)
        review_detail = {
            'product_id' : review.get('product'),
            'rating'     : float(review.get('rate_avg')),
            'rating_img' : star.get(purpose = 'five star').info \
            if float(review.get('rate_avg')) > 4.3  else star.get(purpose = 'four star').info \
            if float(review.get('rate_avg')) < 3.5  else star.get(purpose = 'three star').info,
            'review_count' : review.get('review_count'),
        }
        return JsonResponse({'review_detail' : review_detail}, status = 200)
