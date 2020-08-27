from django.urls import path
from .views import BodyResourceView, FooterResourceView

urlpatterns = [
    path('/body', BodyResourceView.as_view()),
    path('/footer', FooterResourceView.as_view()),
]
