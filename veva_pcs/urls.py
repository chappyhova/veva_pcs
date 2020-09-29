from django.contrib import admin
from django.urls import path
from . import views
from .views import ProductDetailView, ProductListView

urlpatterns = [
    path('', views.home, name='veva-pcs-home'),
    path('about/', views.about, name='veva-pcs-about'),
    path('basket/', views.basket, name='veva-pcs-basket'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('<slug:slug>/', views.update_basket, name='update_basket'),
    path('instagram/', views.instagram, name='veva-pcs-instagram'),
    path('facebook/', views.facebook, name='veva-pcs-facebook'),
    path('twitter/', views.twitter, name='veva-pcs-twitter'),
    path('products/', views.products, name='veva-pcs-products')
]
