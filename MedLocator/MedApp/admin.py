from django.contrib import admin
from .models import StoreItem,StoreCategory

# Register your models here.

admin.site.register(StoreItem)
admin.site.register(StoreCategory)