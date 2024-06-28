from django.contrib import admin

# Register your models here.

from .models import Service, Hotel, Travel, Category, Product, Retreview


admin.site.register([Service, Hotel, Travel, Category, Product, Retreview])
