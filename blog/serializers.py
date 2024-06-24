from rest_framework import serializers
from .models import Car

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io 



class Car:
    def __init__(self, name, brand):
        self.name=name
        self.brand=brand
        
        
new_object_1 = Car(name="Jentra", brand="GM")    


class CarSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=150)
    brand=serializers.CharField()
 
 
 
def serialization():
    print(new_object_1)    
    serializer=CarSerializer(new_object_1)
    print(serializer.data)
    json = JSONRenderer().render(serializer.data)
    print(json)
    
def deserialization():
    json = b'{"name":"Jentra","brand":"GM"}'
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    print(data)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
        
    
    


















# class CarSerializer(serializers.ModelSerializer):
    
    
#     class Meta:
#         model = Car
#         fields = '__all__'

    