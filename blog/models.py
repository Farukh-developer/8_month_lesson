from django.db import models

# Create your models here.

    
    

class Service(models.Model):
    name=models.CharField(max_length=50)
    service_fee=models.IntegerField()
    
    def __str__(self):
        return f"{self.name}"   
    
class Hotel(models.Model):
    name=models.CharField(max_length=100)
    amount_of_star=models.IntegerField(null=True, blank=True)
    price=models.IntegerField(null=True, blank=True)        
    
    def __str__(self):
        return f"{self.name}"          

class Travel(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField(max_length=700)
    date=models.DateTimeField(auto_now_add=True)
    service=models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.name}"    