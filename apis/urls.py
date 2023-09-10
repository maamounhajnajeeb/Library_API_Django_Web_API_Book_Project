from django.urls import path

from . import views

app_name = "apis"

urlpatterns = [
    path("", views.BookAPIView.as_view(), name="book_list_api"),
]
