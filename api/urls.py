from django.urls import path
from api import views

urlpatterns = [
    # path('products/', views.product_list, name='product_list'),
    # path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products_info/', views.product_info, name='product_info'),
    # path('products_list/', views.product_list, name='products_list'),
    path('orders/', views.order_list, name='order_list'),
    path('products_list/', views.ProductList.as_view(), name='products_list'),
    path('products/<int:product_id>/', views.ProductDetail.as_view(), name='product_detail'),

]
