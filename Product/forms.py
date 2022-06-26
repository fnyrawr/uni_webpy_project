from django import forms
from .models import Product, Report, Review

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
        
class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ['type', 'description']
        widgets = {
            'user': forms.HiddenInput(),
            'review': forms.HiddenInput(),
        }