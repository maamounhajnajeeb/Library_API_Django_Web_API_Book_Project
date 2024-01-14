from rest_framework import generics

from books.models import Book
from .serizalizers import BookSerializer

class BookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

