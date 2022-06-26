from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from .forms import ProductForm, ReportForm, ReviewForm
from .models import Product, ProductImage, Review
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = 'all_products'
    template_name = 'product-list.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product-create.html'
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)   
        if form.is_valid():
            product = form.save()
            images = request.FILES.getlist('images')
            pdf = request.FILES.get('pdf')
            
            for image in images:
                ProductImage.objects.create(product=product, image=image)
            
            return redirect('product-detail', pk=product.id)

    def form_valid(self, form):
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'that_one_product'
    template_name = 'product-delete.html'
    success_url = reverse_lazy('product-list')
    
    def post(self, request, **kwargs):
        product_id = kwargs['pk']
        product = Product.objects.get(id=product_id)
        product.pdf.delete()
        product.delete()
        return redirect('product-list')

def product_detail(request, **kwargs):
    product_id = kwargs['pk']
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        user = request.user
        form.instance.user = user
        form.instance.product = product
        print(form)
        if form.is_valid():
            Review.objects.filter(user=user, product = product).delete()
            form.save()
        else:
            print(form.errors) 
    reviews = Review.objects.filter(product=product)
    images = ProductImage.objects.filter(product=product)
    context = {
        'that_one_product': product,
        'product_reviews': reviews,
        'review_form': ReviewForm,
        'product_images': images}
    return render(request, 'product-detail.html', context)
    
def vote_review(request, pk: int, id: int, useful_or_not: str):
    this_review = Review.objects.get(id=id)
    user = request.user
    this_review.vote(user, useful_or_not)
    return redirect('product-detail', pk=pk)

def review_delete(request, **kwargs):
    review_id = kwargs['id']
    if request.method == 'POST':
        Review.objects.filter(id=review_id).delete()
        return redirect('product-detail', pk=kwargs['pk'])
    else:
        review = Review.objects.get(
            id=review_id)
        context = {
            'that_one_review': review}
        return render(request, 'review-delete.html', context)
    
def create_report(request, **kwargs):
    review_id = kwargs['id']
    review = Review.objects.get(
            id=review_id)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        form.instance.user = request.user
        form.instance.review = review
        if form.is_valid():
            form.save()

        return redirect('product-detail', pk=kwargs['pk'])

    else:  # request.method == 'GET'
        form = ReportForm()
        context = {'form': form,
                   'review': review}
        return render(request, 'report-create.html', context)
    
def product_edit(request, **kwargs):
    product_id = kwargs['pk']
    product = Product.objects.get(
            id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        data = form.data
        images = request.FILES.getlist('images')
        pdf = request.FILES.get('pdf')
        if request.FILES.get('pdf'):
            pdf = request.FILES.get('pdf')
            fs = FileSystemStorage(location=settings.PRODUCT_FILES_ROOT, base_url=settings.PRODUCT_FILES_URL)
            file = fs.save(pdf.name, pdf)
            Product.objects.filter(
                id=product_id).update(name=data['name'], description=data['description'], price=data['price'], pdf=settings.PRODUCT_FILES + str(pdf))
        else:
            Product.objects.filter(
                id=product_id).update(name=data['name'], description=data['description'], price=data['price'])
        for image in images:
                ProductImage.objects.create(product=product, image=image)
        return redirect('product-detail', pk=kwargs['pk'])
    else:  # request.method == 'GET'
        form = ProductForm()
        images = ProductImage.objects.filter(product=product)
        context = {'form': form,
                   'product': product,
                   'images': images}
        return render(request, 'product-edit.html', context)
    
def image_delete(request, **kwargs):
    image_id = kwargs['id']
    image = ProductImage.objects.get(id=image_id)
    image.image.delete()
    image.delete()
    return redirect('product-edit', pk=kwargs['pk'])

def pdf_delete(request, **kwargs):
    product_id = kwargs['pk']
    Product.objects.get(id=product_id).pdf.delete()
    return redirect('product-edit', pk=kwargs['pk'])

def review_edit(request, **kwargs):
    review_id = kwargs['id']
    review = Review.objects.get(
            id=review_id)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        data = form.data
        Review.objects.filter(
                id=review_id).update(stars=data['stars'], title=data['title'], text=data['text'])
        return redirect('product-detail', pk=kwargs['pk'])
    else:  # request.method == 'GET'
        form = ReviewForm()
        context = {'form': form,
                   'review': review}
        return render(request, 'review-edit.html', context)