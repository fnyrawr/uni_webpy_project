from email.policy import default
from django import forms
from .models import Product, Report, Review
from django.core.exceptions import ValidationError
class ProductForm(forms.ModelForm):
    # add this if u dont want to do this in html
    #images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'pdf']
        widget = {
           'pdf': forms.FileField()
        }
class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['stars', 'title', 'text']
        widgets = {
            'user': forms.HiddenInput(),
            'timestamp': forms.HiddenInput(),
            'product': forms.HiddenInput(),
        }
    
    def clean_stars(self):
        data = self.cleaned_data['stars']
        if data < 1 or data > 5:
            raise ValidationError("You can only give 1-5 Stars")
        return data
class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ['type', 'description']
        widgets = {
            'user': forms.HiddenInput(),
            'review': forms.HiddenInput(),
            'description': forms.Textarea(),
        }
        
class QuantityForm(forms.Form):
    quantity = forms.IntegerField(initial=1)
    
    def clean_quantity(self):
        data = self.cleaned_data['quantity']
        if data < 1:
            raise ValidationError("You really want to buy this " + str(data) + "x?")
        return data
    
SORT_CHOICES = (
    ('MIN', 'Minimum'),
    ('MAX', 'Maximum'),
    )    
class SearchForm(forms.ModelForm):
    stars = forms.IntegerField(required=False)
    sortStarsBy = forms.ChoiceField(choices = SORT_CHOICES)
    price = forms.IntegerField(initial=None, required=False)
    sortPriceBy = forms.ChoiceField(choices = SORT_CHOICES)
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'sortPriceBy', 'stars', 'sortStarsBy']
