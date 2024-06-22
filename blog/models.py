from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=80)
    engine=models.CharField(max_length=30)
    year=models.DateField()
    
    def __str__(self):
        return f'{self.name}'
    