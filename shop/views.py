from django.shortcuts import render
from .models import Product, Category
from django.http import JsonResponse

def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())}
    return JsonResponse(data)

def category_list(request):
    categories = Category.objects.all()
    data = {"categories": list(categories.values())}
    return JsonResponse(data)