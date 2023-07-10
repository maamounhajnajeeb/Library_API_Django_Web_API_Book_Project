from rest_framework import generics

from django.shortcuts import render

from .serizalizers import BookSerializer
from books.models import Book


# Create your views here.
class BookAPIview(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer