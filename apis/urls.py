from django.urls import path

from .views import BookAPIview

app_name = "apis"

urlpatterns = [
    path("", BookAPIview.as_view(), name="book_list_api"),
]
