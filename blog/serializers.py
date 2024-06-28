from rest_framework import serializers
from .models import Service, Hotel, Travel, Category, Product, Retreview

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io 

class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Service
        fields='__all__'

class TravelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Travel
        fields='__all__'

class HotelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Hotel
        fields='__all__'        

########################################  [[ I wrote this in seraializers.Serializer ]]  ###################################

class CategorySerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=50)
    
    
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.save()
        return instance

# #############################    

class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    price=serializers.IntegerField()
    made_in=serializers.CharField(max_length=100)
    category_id=serializers.IntegerField(read_only=True)
        
     
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.price=validated_data.get('price', instance.price)
        instance.made_in=validated_data.get('made_in', instance.made_in)
        instance.category_id=validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance



# ##############################

class RetreviewSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    product_id=serializers.IntegerField()
    retriew_text=serializers.CharField(max_length=500)
    retriew_rating=serializers.IntegerField(read_only=True)
    
   
    def create(self, validated_data):
       return Retreview.objects.create(**validated_data)
   
    def update(self, instance, validated_data):
        instance.product_id=validated_data.get('product_id', instance.product_id)
        instance.retriew_text=validated_data.get('retriew_text', instance.retriew_text)
        instance.retriew_rating=validated_data.get('retriew_rating', instance.retriew_rating)
        instance.save()
        return instance
    