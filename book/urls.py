
from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_all, name='books_list'),
    # hw2
    path('book/<int:id>/', views.book_detail, name='books_detail'),
]