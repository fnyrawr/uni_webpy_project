from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from Shoppingcart.models import ShoppingCart
# Create your models here.
class CustomUser(AbstractUser):
    ROLES = [
        ('SU', 'Superuser'),
        ('CS', 'Customer service'),
        ('CU', 'Customer'),
    ]
    email = models.EmailField(blank=True, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank = True, null = True)
    role = models.CharField(max_length=2,
                            choices=ROLES,
							default='CU',
                            )
    is_verified = models.BooleanField(default=False)
    
    def count_shopping_cart_items(self):
        count = 0
        shopping_cart = ShoppingCart.objects.filter(user=self)
        
        if shopping_cart:
            shopping_cart = shopping_cart.first()
            print(shopping_cart)
            count = shopping_cart.get_number_of_items()
        
        return count
    
    def is_authorized(self):
        return self.is_superuser_or_customer_service()
    
    def is_superuser_or_customer_service(self):
        if self.role == 'SU' or self.role == 'CS':
            return True
        else:
            return False
        
    def __str__(self):
        return self.username