from django.urls import path

from .views import AllTeaView, RefineView, TeaDetailView

urlpatterns = [
    path('', AllTeaView.as_view()),
    path('/<int:id>', TeaDetailView.as_view()),
    path('/refine', RefineView.as_view()),
]
