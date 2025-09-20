from django.urls import path
from .views import car_list, owner_list

urlpatterns = [
    path('cars/', car_list, name='car_list'),
    path('owners/', owner_list, name='owner_list')
]