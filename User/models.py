from django.db import models
from django.contrib.auth.models import AbstractUser
from Shoppingcart.models import ShoppingCart
# Create your models here.
class CustomUser(AbstractUser):
    ROLES = [
        ('SU', 'superuser'),
        ('CS', 'customer service'),
        ('CU', 'customer'),
        ('BP', 'business partner'),
    ]
    email = models.EmailField(blank=True, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank = True, null = True)
    role = models.CharField(max_length=2,
                            choices=ROLES,
							default='CU',
                            )

    def count_shopping_cart_items(self):
        count = 0
        shopping_cart = ShoppingCart.objects.filter(user=self)
        if shopping_cart:
            shopping_cart = shopping_cart.first()
            count = shopping_cart.get_number_of_items()

        return count