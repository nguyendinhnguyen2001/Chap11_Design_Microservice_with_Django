from django.urls import path
from book_model import views

urlpatterns = [
    path('book/', views.book, name="books"),
    path('book/<int:pk>', views.book_detail,name="book-detail"),
]
