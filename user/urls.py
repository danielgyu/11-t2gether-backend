from django.urls import path

from .views import JoinView, LogInView

urlpatterns = [
    path('join', JoinView.as_view()),
    path('login', LogInView.as_view())
]
