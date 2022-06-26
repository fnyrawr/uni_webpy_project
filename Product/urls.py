from django.urls import path
from . import views

urlpatterns = [
    #Product paths
    path('show/', views.ProductListView.as_view(), name='product-list'),
    path('show/<int:pk>/', views.product_detail, name='product-detail'),
    path('create/', views.ProductCreateView.as_view(), name='product-create'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('edit/<int:pk>', views.product_edit, name='product-edit'),
    path('delete/<int:pk>/pdf', views.pdf_delete, name='pdf-delete'),
    #Review paths
    path('delete/<int:pk>/review/<int:id>', views.review_delete, name='review-delete'),
    path('show/<int:pk>/review/<int:id>/vote/<str:useful_or_not>', views.vote_review, name='review-vote'),
    path('show/<int:pk>/review/<int:id>/report', views.create_report, name='create-report'),
    path('edit/<int:pk>/review/<int:id>', views.review_edit, name='review-edit'),

    #Image paths
    path('delete/<int:pk>/image/<int:id>', views.image_delete, name='image-delete'),
    #maybe CustomerService paths later
]