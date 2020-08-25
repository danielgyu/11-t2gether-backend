from django.urls import path

from .views import AllTeaView, RefineView, TeaDetailView

urlpatterns = [
    path('/all', AllTeaView.as_view()),
    path('/refine', RefineView.as_view()),
    path('/detail/<int:id>', TeaDetailView.as_view()),
]
