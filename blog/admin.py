from django.contrib import admin

# Register your models here.

from .models import Service, Hotel, Travel


admin.site.register([Service, Hotel, Travel])
