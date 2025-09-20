from django.urls import path
from .views import product_list, category_list

urlpatterns = [
    path("categories/", category_list, name='category_list'),
    path("products/", product_list, name="product_list"),
]