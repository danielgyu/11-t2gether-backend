from django.urls import path

from .views import AllTeaView

urlpatterns = [
    path('/all', AllTeaView.as_view()),
]
