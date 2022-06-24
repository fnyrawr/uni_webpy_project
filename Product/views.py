from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from webpyproject.Product.forms import ProductForm, ReviewForm
from .models import Product, Review
# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = 'all_products'  # Default: object_list
    template_name = 'product-list.html'  # Default: book_list.html

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product-create.html'
    
    def get_success_url(self):
        # muss noch getestet werden
        return reverse('product-detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'that_one_product'
    template_name = 'product-delete.html'
    success_url = reverse_lazy('product-list')

def product_detail(request, **kwargs):
    # print(kwargs)
    product_id = kwargs['pk']
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        form.instance.user = request.user
        form.instance.product = product
        if form.is_valid():
            form.save()
        else:
            print(form.errors) 
    reviews = Review.objects.filter(product=product)
    context = {
        'that_one_product': product,
        'product_reviews': reviews,
        'review_form': ReviewForm}
    return render(request, 'product-detail.html', context)
    
def vote_review(request, pk: int, id: int, useful_or_not: str):
    this_review = Review.objects.get(id=id)
    user = request.user
    this_review.vote(user, useful_or_not)
    return redirect('product-detail', pk=pk)
