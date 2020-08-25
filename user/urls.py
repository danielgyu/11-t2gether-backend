from django.urls import path

from .views import (
    JoinView,
    LogInView,
    WishlistView
)

urlpatterns = [
    path('/join', JoinView.as_view()),
    path('/login', LogInView.as_view()),
    path('/wishlist', WishlistView.as_view())
]
