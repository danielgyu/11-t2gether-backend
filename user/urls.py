from django.urls import path

from .views import (
    JoinView,
    LogInView,
    UseWishlistView
)

urlpatterns = [
    path('/join', JoinView.as_view()),
    path('/login', LogInView.as_view()),
    path('/wishlist', UseWishlistView.as_view())
]
