from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Car
from .serializers import CarSerializer
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework.request import Request

from rest_framework.response import Response


# class CarAPIView(ListAPIView):
    
#     queryset=Car.objects.all()
#     serializer_class=CarSerializer
    
    
# ############ Getting an object product (id=id, 1+1) information   

class CarDetailView(RetrieveAPIView):
    
    queryset=Car.objects.all()
    serializer_class=CarSerializer

class CarAPIView(APIView):
    def get(self, request: Request):
        car=Car.objects.values()
        return Response({'car':car})
    

    def post(self, request: Request):
        car=Car.objects.create(
            name=request.data['name'],
            brand=request.data['brand'],
            engine=request.data['engine'],
            year=request.data['year'],
        )
        return Response(model_to_dict(car))
    
    

