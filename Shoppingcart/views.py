from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from Shoppingcart.main import PDF
from .forms import CreditCardForm, GiroCardForm, PaymentForm
from .models import Payment, ShoppingCart, ShoppingCartItem
from django.conf import settings

def show_shopping_cart(request):
    if request.method == 'POST':
        if 'empty' in request.POST:
            ShoppingCart.objects.get(user=request.user).delete()

            context = {'shopping_cart_is_empty': True,
                       'shopping_cart_items': None,
                       'amount': 0.0}
            return render(request, 'shopping-cart.html', context)

        elif 'pay' in request.POST:
            return redirect('shopping-cart-pay')

    else:  # request.method == 'GET'
        shopping_cart_is_empty = True
        shopping_cart_items = None
        total = Decimal(0.0)  # Default without Decimal() would be type float!

        user = request.user
        if user.is_authenticated:
            shopping_cart = ShoppingCart.objects.filter(user=user)
            if shopping_cart:
                shopping_cart = shopping_cart.first()
                shopping_cart_is_empty = False
                shopping_cart_items = ShoppingCartItem.objects.filter(shopping_cart=shopping_cart)
                total = shopping_cart.get_total()

        context = {'shopping_cart_is_empty': shopping_cart_is_empty,
                   'shopping_cart_items': shopping_cart_items,
                   'total': total}
        return render(request, 'shopping-cart.html', context)

@login_required(login_url='/useradmin/login/')
def pay(request, **kwargs):
    payment = None
    shopping_cart_is_empty = True
    paid = False
    user = request.user
    shopping_cart = ShoppingCart.objects.filter(user=user)
    if shopping_cart:
        shopping_cart = shopping_cart.first()
        shopping_cart_is_empty = False
    form = PaymentForm(initial={'amount': shopping_cart.get_total()})
    payment_type_form = None
    
    if request.method == 'POST':
        if 'pay' in request.POST:
            payment_method = None
            if 'credit_card_number' in request.POST:
                payment_method = "C"
                payment_type_form = CreditCardForm(request.POST)
            else:
                payment_method = "G"
                payment_type_form = GiroCardForm(request.POST)
            
            payment_type_form.instance.user = user
            if(payment_type_form.is_valid()):
                payment_type_form.save()
                amount = shopping_cart.get_total()

                item_set = ShoppingCartItem.objects.filter(shopping_cart=shopping_cart)
                data2 = [(str(item.quantity) +"x " + str(item.product.name), item.get_itemSum()) for item in item_set]
                
                payment = Payment.objects.create(payment_method=payment_method,
                                       amount= amount, 
                                       user = user,
                                       )
                PDF('P', 'mm', 'Letter', data=data2, user=user.username, email=user.email, payment = payment.get_payment(), payment_id = payment.id)
                payment.pdf = settings.INVOICE_FILES + user.username + str(payment.id) + "Invoice.pdf"
                paid = True
                ShoppingCart.objects.get(user=user).delete()
            else:
                print(payment_type_form.errors)

        else:
            form = PaymentForm(request.POST, initial={'user': user})
            form.instance.user = user
            if form.is_valid():
                    data = form.cleaned_data
                    payment_type = data['payment_method']
                    if payment_type == 'G':
                        payment_type_form = GiroCardForm
                    elif payment_type == 'C':
                        payment_type_form = CreditCardForm
                    else:
                        return redirect('https://www.paypal.com/signin')
            else:
                print(form.errors)
        shopping_cart_is_empty = False
    context = {'shopping_cart_is_empty': shopping_cart_is_empty,
               'payment_form': form,
               'paid': paid,
               'payment_type_form': payment_type_form,
               'payment': payment}
    return render(request, 'pay.html', context)

def delete_item(request, **kwargs):
        item_id = kwargs['pk']
        ShoppingCartItem.objects.filter(id=item_id).delete()
        shopping_cart = ShoppingCart.objects.filter(user = request.user).first()
        cart_items = ShoppingCartItem.objects.filter(shopping_cart=shopping_cart)
        if not cart_items:
            shopping_cart.delete()
        return redirect('shopping-cart-show')