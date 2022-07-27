from decimal import Decimal
from django.conf import settings
from django.db import models
from django.utils import timezone
from Product.models import Product

class ShoppingCart(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               )

    def add_item(user, product, quantity):
        # Get existing shopping cart, or create a new one if none exists
        shopping_cart = ShoppingCart.objects.filter(user=user)
        if shopping_cart:
            shopping_cart = shopping_cart.first()
        else:
            shopping_cart = ShoppingCart.objects.create(user=user)
        # Add product to shopping cart
        ShoppingCartItem.add_quantity(shopping_cart, product, quantity)
    
    def get_number_of_items(self):
        shopping_cart_items = ShoppingCartItem.objects.filter(shopping_cart=self)
        items = 0
        for item in shopping_cart_items:
            items += item.quantity
        return items

    def get_total(self):
        total = Decimal(0.0)  # Default without Decimal() would be type float!
        shopping_cart_items = ShoppingCartItem.objects.filter(shopping_cart=self)
        for item in shopping_cart_items:
            total += item.product.price * item.quantity
        return total

    def __str__(self):
        return str(self.timestamp) + " from " + self.user.username
    
    def __repr__(self):
        return str(self.timestamp) + " from " + self.user.username

class ShoppingCartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)

    def add_quantity(shopping_cart, product, quantity):
        item = ShoppingCartItem.objects.filter(shopping_cart=shopping_cart, product=product)
        if item:
            item = item.first()
            ShoppingCartItem.objects.filter(id= item.id).update(quantity= item.quantity + quantity)
        else:
            ShoppingCartItem.objects.create(product = product,
                                        quantity=quantity,
                                        shopping_cart=shopping_cart)
    
    def get_itemSum(self):
        sum = Decimal(0.0)  # Default without Decimal() would be type float!
        sum = self.quantity * self.product.price
        return sum
    
    def __str__(self):
        return self.product + " quantity " + self.quantity + " for " + self.shopping_cart
    
    def __repr__(self):
        return self.product + " quantity " + self.quantity + " for " + self.shopping_cart

class Payment(models.Model):
    PAYMENT_TYPES = [
        ('C', 'Creditcard'),
        ('P', 'Paypal'),
        ('G', 'Girocard'),
    ]
    
    payment_method = models.CharField(max_length=1, choices=PAYMENT_TYPES)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    timestamp = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               null = True, blank = True)
    pdf = models.FileField(upload_to='invoices/', null= True, blank=True)
    
    def get_payment(self):
        if(self.payment_method == 'C'):
            c = CreditCard.objects.filter(user=self.user).first()
            info = c.credit_card_number
        else:
            g=GiroCard.objects.filter(user=self.user).first()
            info = g.iban

        return dict(self.PAYMENT_TYPES)[self.payment_method] + " | " + info
    
#user can safe his credit card infos
class CreditCard(models.Model):
    credit_card_number = models.CharField(max_length=19)  # Format: 1234 5678 1234 5678
    expiry_date = models.CharField(max_length=7)  # Format: 10/2022
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)

#user can safe his giro card infos
class GiroCard(models.Model):
    iban = models.CharField(max_length=27)  # Format: DE22 2222 2222 2222 2222 22
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)