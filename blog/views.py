from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Service, Hotel, Travel
from .serializers import ServiceSerializer, HotelSerializer, TravelSerializer
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework.request import Request

from rest_framework.response import Response


class ServiceAPIView(APIView):
    def get(self, request: Request, pk = None):
        if pk:
            try:
                service=Service.objects.get(pk=pk)
                return Response(ServiceSerializer(service).data)   
            except: 
                return Response({'message':'data not found'})
            
        service=Service.objects.all()
        return Response({'service':ServiceSerializer(service, many=True).data})
    
    def post(self, request: Request):
        serializer=ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service=serializer.save()
        return Response(ServiceSerializer(service).data)
    
        
    def put(self, request: Request, pk: int = None):
        if not pk:
            return Response({'message':'PUT methos is not allowed'})
        try:
            service=Service.objects.get(pk=pk)
            serializer=ServiceSerializer(instance=service, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_service=serializer.save()
            return Response(ServiceSerializer(updated_service).data)
        except:
            return Response({'message':'data not found'})
            
        
    
    def delete(self, request: Request, pk: int = None):
        if not pk:
            return Response({'message':'Delete methos is not allowed'})
        try:
            service=Service.objects.get(pk=pk)
            service.delete()
            return Response({"message":"Removed by you"})
        except:
            return Response({'message':'data not found'})
        
        
##################### 2

class HotelAPIView(APIView):
    def get(self, request: Request, pk = None):
        if pk:
            try:
                hotel=Hotel.objects.get(pk=pk)
                return Response(HotelSerializer(hotel).data)   
            except: 
                return Response({'message':'data not found'})
            
        hotel=Hotel.objects.all()
        return Response({'hotel':HotelSerializer(hotel, many=True).data})
    
    def post(self, request: Request):
        serializer=HotelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        hotel=serializer.save()
        return Response(HotelSerializer(hotel).data)
    
        
    def put(self, request: Request, pk: int = None):
        if not pk:
            return Response({'message':'PUT methos is not allowed'})
        try:
            hotel=Hotel.objects.get(pk=pk)
            serializer=HotelSerializer(instance=hotel, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_hotel=serializer.save()
            return Response(HotelSerializer(updated_hotel).data)
        except:
            return Response({'message':'data not found'})
            
        
    
    def delete(self, request: Request, pk: int = None):
        if not pk:
            return Response({'message':'Delete methos is not allowed'})
        try:
            hotel=Hotel.objects.get(pk=pk)
            hotel.delete()
            return Response({"message":"Removed by you"})
        except:
            return Response({'message':'data not found'})
        
        
##################### 3


class TravelAPIView(APIView):
    def get(self, request: Request, pk = None):
        if pk:
            try:
                travel=Travel.objects.get(pk=pk)
                return Response(TravelSerializer(travel).data)   
            except: 
                return Response({'message':'data not found'})
            
        travel=Travel.objects.all()
        return Response({'travel':TravelSerializer(travel, many=True).data})
    
    
    def post(self, request: Request):
        serializer=TravelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        travel=serializer.save()
        return Response(TravelSerializer(travel).data)
    
        
    def put(self, request: Request, pk: int = None):
        if not pk:
            return Response({'message':'PUT methos is not allowed'})
        try:
            travel=Travel.objects.get(pk=pk)
            serializer=TravelSerializer(instance=travel, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_travel=serializer.save()
            return Response(TravelSerializer(updated_travel).data)
        except:
            return Response({'message':'data not found'})
            
        
    
    def delete(self, request: Request, pk: int = None):
        if not pk:
            return Response({'message':'Delete methos is not allowed'})
        try:
            travel=Travel.objects.get(pk=pk)
            travel.delete()
            return Response({"message":"Removed by you"})
        except:
            return Response({'message':'data not found'})
        
        
    