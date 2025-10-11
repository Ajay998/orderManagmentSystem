from django.urls import path
from api import views

urlpatterns = [
    path('products_info/', views.product_info, name='product_info'),
    path('orders/', views.OrderList.as_view(), name='order_list'),
    path('products_list/', views.ProductList.as_view(), name='products_list'),
    path('products/<int:product_id>/', views.ProductDetail.as_view(), name='product_detail'),
    path('user-orders/', views.UserOrderListAPIView.as_view(), name='user_orders'),

]
