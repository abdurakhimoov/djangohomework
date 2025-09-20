from django.urls import path
from .views import order_list, orderItem_list

urlpatterns = [
    path("orders/", order_list, name='order_list'),
    path("orderItems/", orderItem_list, name='orderItem_list'),
]