from django.contrib import admin

# Register your models here.

from .models import Products, Products_Sale, All_Products, Customer, Personal_cart, Cart_item
admin.site.register(Products)
admin.site.register(Products_Sale)
admin.site.register(All_Products)
admin.site.register(Customer)
admin.site.register(Personal_cart)
admin.site.register(Cart_item)