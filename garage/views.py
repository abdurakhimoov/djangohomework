from django.shortcuts import render
from django.http import JsonResponse
from .models import Owner, Car

def owner_list(requrst):
    owners = Owner.objects.all()
    data = {"owners": list(owners.values())}
    return JsonResponse(data)

def car_list(request):
    cars = Car.objects.all()
    data = {"cars": list(cars.values())}
    return JsonResponse(data)