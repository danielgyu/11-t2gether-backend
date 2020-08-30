from django.urls import path, include

urlpatterns = [
    path('user', include('user.urls')),
    path('products', include('product.urls')),
    path('reviews', include('review.urls')),
    path('main', include('main.urls')),
]
