from django.shortcuts import render
from .models import Book
from django.http import JsonResponse


def book_list(request):
    books = Book.objects.all()
    data = {'books': list(books.values())}
    return JsonResponse(data)