from django.urls import path
from .views import ProductList, ProductDetail

app_name = 'shop'

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('<slug:category_slug>', ProductList.as_view(), name='product-list-by-cat'),
    path('<int:pk>/<slug:slug>', ProductDetail.as_view(), name='product-detail'),
]