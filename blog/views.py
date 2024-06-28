from django.shortcuts import render
from rest_framework.generics import  RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, ListAPIView
from .models import Service, Hotel, Travel, Category, Product, Retreview
from .serializers import ServiceSerializer, HotelSerializer, TravelSerializer, CategorySerializer, ProductSerializer, RetreviewSerializer
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.request import Request

from rest_framework.response import Response


class ListCreateServiceAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    queruset = Service.objects.all()
    serializer_class=ServiceSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    
class RetrieveServiceUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   GenericAPIView):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer
    
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
################################################################## 2



class ListCreateHotelAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    queryset = Hotel.objects.all()
    serializer_class=HotelSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    
class RetrieveHotelUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   GenericAPIView):
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer
    
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    
    
    
################################################# 3

class ListCreateTravelAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    queruset = Travel.objects.all()
    serializer_class=TravelSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    
class RetrieveTravelUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   GenericAPIView):
    queryset=Travel.objects.all()
    serializer_class=TravelSerializer
    
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)        
    
    
    
    
############################################ View in generic views methods
    
class ListCategoryAPIView(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
    
class ListUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
###################################### 2


class ListProductAPIView(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=CategorySerializer
    
    
class ListUpdateProductDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    
#################################### 3



class ListRetriewCreateAPIView(ListCreateAPIView):
    queryset=Retreview.objects.all()
    serializer_class=RetreviewSerializer
    
    
class ListUpdateRetriewDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Retreview.objects.all()
    serializer_class=RetreviewSerializer
    
    
    
       
        