from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Car
from .serializers import CarSerializer


class CarAPIView(ListAPIView):
    
    queryset=Car.objects.all()
    serializer_class=CarSerializer
    
    
############ Getting an object product (id=id, 1+1) information   

class CarDetailView(RetrieveAPIView):
    
    queryset=Car.objects.all()
    serializer_class=CarSerializer
    
    

