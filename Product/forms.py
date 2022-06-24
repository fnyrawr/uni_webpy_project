from django import forms
from .models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'pdf']
        
class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['stars', 'title', 'text']
        widgets = {
            'user': forms.HiddenInput(),
            'timestamp': forms.HiddenInput(),
            'product': forms.HiddenInput(),
        }