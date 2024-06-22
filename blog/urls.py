from django.urls import path
from .views import CarAPIView, CarDetailView

urlpatterns = [
    path('api/v1/car/', CarAPIView.as_view()),
    path('api/v1/car/<int:pk>/', CarDetailView.as_view()),
]



