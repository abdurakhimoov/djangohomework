from django.shortcuts import render
from django.http import JsonResponse
from .models import Order, OrderItem

def order_list(request):
    orders = Order.objects.all()
    data = {"orders": list(orders.values())}
    return JsonResponse(data)

def orderItem_list(request):
    orderItems = OrderItem.objects.all()
    data = {"orderItems": list(orderItems.values())}
    return JsonResponse(data)