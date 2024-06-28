from django.urls import path
from .views import ( ListCreateServiceAPIView, RetrieveServiceUpdateDestroyAPIView, ListCreateHotelAPIView, 
                    RetrieveHotelUpdateDestroyAPIView, ListCreateTravelAPIView, RetrieveTravelUpdateDestroyAPIView, ListCategoryAPIView, ListUpdateDestroyAPIView, 
                    ListProductAPIView, ListUpdateProductDestroyAPIView, ListRetriewCreateAPIView, ListUpdateRetriewDestroyAPIView)
urlpatterns = [
    
    
    
    
    
    path('api/v1/service/', ListCreateServiceAPIView.as_view()),
    path('api/v1/service/<int:pk>/', RetrieveServiceUpdateDestroyAPIView.as_view()),
    
    # 1 ########################################################### 
    
    path('api/v1/hotel/', ListCreateHotelAPIView.as_view()),
    path('api/v1/hotel/<int:pk>/', RetrieveHotelUpdateDestroyAPIView.as_view()),
    
    # 2 ########################################################## 
    
    path('api/v1/travel/', ListCreateTravelAPIView.as_view()),
    path('api/v1/travel/<int:pk>/', RetrieveTravelUpdateDestroyAPIView.as_view()),
    
    # Generics urls
    
    path('api/v1/categroy/', ListCategoryAPIView.as_view()),
    path('api/v1/categroy/<int:pk>/', ListUpdateDestroyAPIView.as_view()),
    
    
    path('api/v1/product/', ListProductAPIView.as_view()),
    path('api/v1/product/<int:pk>/', ListUpdateProductDestroyAPIView.as_view()),
    
    path('api/v1/retriew/', ListRetriewCreateAPIView.as_view()),
    path('api/v1/retriew/<int:pk>/', ListUpdateRetriewDestroyAPIView.as_view()),
    
    
]



