from rest_framework import serializers
from .models import Service, Hotel, Travel

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io 

class ServiceSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=50)
    service_fee=serializers.IntegerField()
    
    
    def create(self, validated_data):
        return Service.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.service_fee=validated_data.get('service_fee', instance.service_fee)
        instance.save()
        return instance

#############################    

class HotelSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    amount_of_star=serializers.IntegerField()
    price=serializers.IntegerField(read_only=True)
        
     
    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.amount_of_star=validated_data.get('amount_of_star', instance.amount_of_star)
        instance.price=validated_data.get('price', instance.price)
        instance.save()
        return instance



##############################

class TravelSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=150)
    description=serializers.CharField(max_length=700)
    date=serializers.DateTimeField()
    service_id=serializers.CharField(max_length=100)
    hotel_id=serializers.CharField(max_length=100)
   
    def create(self, validated_data):
       return Travel.objects.create(**validated_data)
   
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.description=validated_data.get('description', instance.description)
        instance.date=validated_data.get('date', instance.date)
        instance.service_id=validated_data.get('service_id', instance.service_id)
        instance.hotel_id=validated_data.get('hotel_id', instance.hotel_id)
        instance.save()
        return instance
    