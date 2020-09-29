from django.contrib import admin
from .models import Product, Basket, BasketItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

admin.site.register(Product, ProductAdmin)
admin.site.register(Basket)
admin.site.register(BasketItem)