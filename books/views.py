from django.shortcuts import render
from django.views.generic import ListView

from .models import Book
# Create your views here.

class BooksListView(ListView):
    model = Book
    template_name = "book_list.html"
    # we get the object name by <model name>_<Generic class view main name>