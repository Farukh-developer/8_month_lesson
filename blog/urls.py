from django.urls import path
from .views import ServiceAPIView, HotelAPIView, TravelAPIView
urlpatterns = [
    
    
    
    
    
    path('api/v1/service/', ServiceAPIView.as_view()),
    path('api/v1/service/<int:pk>/', ServiceAPIView.as_view()),
    
    ###########################################################
    
    path('api/v1/hotel/', HotelAPIView.as_view()),
    path('api/v1/hotel/<int:pk>/', HotelAPIView.as_view()),
    
    ###########################################################
    
    path('api/v1/travel/', TravelAPIView.as_view()),
    path('api/v1/travel/<int:pk>/', TravelAPIView.as_view()),
    
    
]



