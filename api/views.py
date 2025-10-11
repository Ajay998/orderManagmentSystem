from api.serializers import ProductInfoSerializer, ProductSerializer, OrderSerializer
from rest_framework import generics
from api.models import Product, Order
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Max
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

class OrderList(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer

class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(user=user)



@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    count = products.count()
    serializer = ProductInfoSerializer({
        'product': products,
        'count': count,
        'max_price': products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data)

