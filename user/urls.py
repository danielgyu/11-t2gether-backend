from django.urls import path

from .views import (
    JoinView,
    LogInView,
    WishlistView,
    ShoppingBagView
)

urlpatterns = [
    path('/join', JoinView.as_view()),
    path('/login', LogInView.as_view()),
    path('/wishlist', WishlistView.as_view()),
    path('/shoppingbag', ShoppingBagView.as_view())
]
