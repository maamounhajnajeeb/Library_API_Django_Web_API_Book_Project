from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book

# Create your tests here.

class APITest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title="Django For APIs",
            subtitle="Build web APIs with Python & Django",
            author="William S Vincent",
            isbn="9781735467221",
        )
    
    def test_api_listview(self):
        response = self.client.get(reverse("apis:book_list_api"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        # self.assertEqual(response, self.book)
        