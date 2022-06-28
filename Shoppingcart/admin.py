from django.contrib import admin
from .models import Payment, ShoppingCart, ShoppingCartItem

# Register your models here.
admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)
admin.site.register(Payment)