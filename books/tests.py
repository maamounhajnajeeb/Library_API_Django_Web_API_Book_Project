from django.test import TestCase
from django.urls import reverse

from .models import Book
# Create your tests here.

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django For Beginners", subtitle="Django Defentive Guide",
            author="William S Vincent", isbn="1236547893210",
        )
    
    def test_content(self):
        book = self.book
        self.assertTrue(book.title == "Django For Beginners")
        self.assertEqual(book.subtitle, "Django Defentive Guide")
        self.assertEqual(book.author, "William S Vincent")
        self.assertTrue(book.isbn == "1236547893210")
    
    def test_books_listview(self):
        response = self.client.get(reverse("books:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django For Beginners")
        self.assertTemplateUsed(response, "books/book_list.html")