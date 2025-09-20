from django.shortcuts import render
from django.http import JsonResponse
from .models import Create_profile, Login

def createP_list(request):
    create_profiles = Create_profile.objects.all()
    data = {"users": list(create_profiles.values())}
    return JsonResponse(data)


def login_list(request):
    logins = Login.objects.all()
    data = {"users": list(logins.values())}
    return JsonResponse(data)