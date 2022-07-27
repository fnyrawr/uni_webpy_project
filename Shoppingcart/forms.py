from django import forms
from .models import CreditCard, GiroCard, Payment, ShoppingCartItem
from django.core.exceptions import ValidationError
import re

class PaymentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs['readonly'] = True

    class Meta:
        model = Payment
        fields = ['payment_method', 'amount']
        widgets = {
            'payment_method': forms.Select(choices=Payment.PAYMENT_TYPES),
            'user': forms.HiddenInput(),
        }
class PaymentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs['readonly'] = True

    class Meta:
        model = Payment
        fields = ['payment_method', 'amount']
        widgets = {
            'payment_method': forms.Select(choices=Payment.PAYMENT_TYPES),
            'user': forms.HiddenInput(),
        }
class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['credit_card_number', 'expiry_date']
        widgets = {
            'user': forms.HiddenInput(),
        }
        
    def clean_expiry_date(self):
        data = self.cleaned_data['expiry_date']
        #data without spaces
        match = re.search(r'(0{0,1}[1-9]{1}|1{1}[0-2]{1})/\d{4}' , data)
        if not match:
            raise ValidationError("Your expiration date is in a wrong format")
        
        return data
    
    def clean_credit_card_number(self):
        data = self.cleaned_data['credit_card_number']
        #data without spaces
        data = data.replace(" ", "")
        match = re.search(r'\d{16}' , data)
        if not match:
            raise ValidationError("Your credit card number is wrong!")
        
        return data
class GiroCardForm(forms.ModelForm):
    class Meta:
        model = GiroCard
        fields = ['iban']
        widgets = {
            'user': forms.HiddenInput(),
        }
        
    def clean_iban(self):
        data = self.cleaned_data['iban']
        #data without spaces
        data = data.replace(" ", "")
        match = re.search(r'[A-Z]{2}\d{20}' , data)
        if not match:
            raise ValidationError("Your iban is in a wrong format")
        
        return data