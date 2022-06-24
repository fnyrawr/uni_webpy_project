from django.urls import path
from . import views

urlpatterns = [
    #Product paths
    path('show/', views.product_list, name='product-list'),
    path('show/<int:pk>/', views.product_detail, name='product-detail'),
    path('create/', views.product_create, name='product-create'),
    path('edit/<int:pk>', views.product_edit, name='product-detail'),
    path('delete/<int:pk>/', views.product_delete, name='product-delete'),
    #Review paths
    path('delete/<int:pk>/review', views.review_delete, name='review-delete'),
    path('show/<int:pk>/review/<int:id>/vote/<str:useful_or_not>/', views.vote_comment, name='comment-vote'),
    path('show/<int:pk>/review', views.create_review, name='comment-vote'),
    path('show/<int:pk>/report', views.create_report, name='comment-report'),
    path('edit/<int:pk>/review/<int:id>', views.product_delete, name='product-delete'),
    path('show/<int:pk>/vote/<int:id>/<str:up_or_down>/', views.vote_comment, name='comment-vote'),
]